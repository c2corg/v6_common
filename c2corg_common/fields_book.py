DEFAULT_FIELDS = [
    'locales.title',
    'locales.summary',
    'locales.description',
    'locales.lang',
    'author',
    'editor',
    'activities',
    'url',
    'isbn',
    'book_types',
    'publication_date',
    'nb_pages'
]

DEFAULT_REQUIRED = [
    'locales',
    'locales.title',
    'book_types'
]

LISTING_FIELDS = [
    'locales',
    'locales.title',
    'locales.description',
    'activities',
    'author',
    'quality',
    'publication_date',
    'book_types'
]

fields_book = {
    'fields': DEFAULT_FIELDS,
    'required': DEFAULT_REQUIRED,
    'listing': LISTING_FIELDS
}
