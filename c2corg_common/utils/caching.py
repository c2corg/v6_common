""" Caching related helper functions shared between UI and API.
"""

import time
import logging
from dogpile.cache.api import NO_VALUE

log = logging.getLogger(__name__)

# the current status (up/down) of the cache
cache_status = None


def initialize_cache_status(refresh_period):
    global cache_status
    cache_status = CacheStatus(refresh_period)


def get_or_create(cache, key, creator):
    """ Try to get the value for the given key from the cache. In case of
    errors fallback to the creator function (e.g. load from the database).
    """
    if cache_status.is_down():
        log.warn('Not getting value from cache because it seems to be down')
        return creator()

    try:
        value = cache.get_or_create(
            key, creator_wrapper(creator), expiration_time=-1)
        cache_status.request_success()
        return value
    except CreatorException as creator_exception:
        raise creator_exception.exc
    except:  # noqa
        log.error('Getting value from cache failed', exc_info=True)
        cache_status.request_failure()
        return creator()


def get_or_create_multi(cache, keys, creator, should_cache_fn=None):
    """ Try to get the values for the given keys from the cache. In case of
    errors fallback to the creator function (e.g. load from the database).
    """
    if cache_status.is_down():
        log.warn('Not getting values from cache because it seems to be down')
        return creator(*keys)

    try:
        values = cache.get_or_create_multi(
            keys, creator_wrapper(creator), expiration_time=-1,
            should_cache_fn=should_cache_fn)
        cache_status.request_success()
        return values
    except CreatorException as creator_exception:
        raise creator_exception.exc
    except:  # noqa
        log.error('Getting values from cache failed', exc_info=True)
        cache_status.request_failure()
        return creator(*keys)


def get(cache, key):
    """ Try to get the value for the given key from the cache. In case of
    errors, return NO_VALUE.
    """
    if cache_status.is_down():
        log.warn('Not getting value from cache because it seems to be down')
        return NO_VALUE

    try:
        value = cache.get(key, ignore_expiration=True)
        cache_status.request_success()
        return value
    except:  # noqa
        log.error('Getting value from cache failed', exc_info=True)
        cache_status.request_failure()
        return NO_VALUE


def set(cache, key, value):
    """ Try to set the value with the given key in the cache. In case of
    errors, log the error and continue.
    """
    if cache_status.is_down():
        log.warn('Not setting value in cache because it seems to be down')
        return

    try:
        cache.set(key, value)
        cache_status.request_success()
    except:  # noqa
        log.error('Setting value in cache failed', exc_info=True)
        cache_status.request_failure()


class CreatorException(Exception):
    """ An exception happening during the execution of a cache `creator`
    function.
    """
    def __init__(self, exc):
        self.exc = exc


def creator_wrapper(creator):
    """ A wrapper around `creator` functions. The purpose of this wrapper is
    to distinguish exceptions caused in creator functions from exceptions
    while trying to read a value from the cache.
    """
    def fn(*args, **kwargs):
        try:
            return creator(*args, **kwargs)
        except Exception as exc:
            raise CreatorException(exc)
    return fn


class CacheStatus(object):
    """ To avoid that requests are made to the cache if it is down, the status
    of the last requests is stored. If a request in the 30 seconds failed,
    no new request will be made.
    """

    def __init__(self, refresh_period=30):
        self.up = True
        self.status_time = time.time()
        self.refresh_period = refresh_period

    def is_down(self):
        if self.up:
            return False

        # no request is made to the cache if it is down. but if the cache
        # status should be refreshed, a request is made even though it was
        # down before.
        should_refresh = time.time() - self.status_time > self.refresh_period
        return not should_refresh

    def request_failure(self):
        self.up = False
        self.status_time = time.time()

    def request_success(self):
        self.up = True
        self.status_time = time.time()
