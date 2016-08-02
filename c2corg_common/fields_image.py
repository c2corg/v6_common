DEFAULT_FIELDS = [
    'locales.title',
    'locales.summary',
    'locales.description',
    'geometry.geom',
    'activities',
    'categories',
    'image_type',
    'author',
    'has_svg',
    'elevation',
    'height',
    'width',
    'file_size',
    'filename',
    'camera_name',
    'exposure_time',
    'focal_length',
    'fnumber',
    'iso_speed',
    'quality'
]

DEFAULT_REQUIRED = [
    'locales',
    'locales.title',
    'image_type'
]

LISTING_FIELDS = [
    'locales.title',
    'geometry.geom',
    'filename',
    'activities',
    'image_type',
    'elevation',
    'iso_speed',
    'quality',
    'camera_name',
    'exposure_time',
    'focal_length',
    'categories',
    'fnumber'
]

fields_image = {
    'fields': DEFAULT_FIELDS,
    'required': DEFAULT_REQUIRED,
    'listing': LISTING_FIELDS
}
