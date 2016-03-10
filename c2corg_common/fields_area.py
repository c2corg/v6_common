DEFAULT_FIELDS = [
    'locales.title',
    'geometry.geom',
    'area_type'
]

DEFAULT_REQUIRED = [
    'locales',
    'locales.title',
    'geometry',
    'geometry.geom',
    'area_type'
]

LISTING_FIELDS = [
    'locales.title',
    'area_type'
]

fields_area = {
    'fields': DEFAULT_FIELDS,
    'required': DEFAULT_REQUIRED,
    'listing': LISTING_FIELDS
}
