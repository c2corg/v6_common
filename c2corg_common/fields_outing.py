# Common attributes settings used by most outing activities
DEFAULT_FIELDS = [
    'locales.title',
    'locales.summary',
    'locales.description',
    'locales.topic_id',
    'locales.participants',
    'locales.access_comment',
    'locales.weather',
    'locales.timing',
    'locales.conditions_levels',
    'locales.conditions',
    'locales.hut_comment',
    'locales.route_description',
    'geometry.geom',
    'geometry.geom_detail',
    'activities',
    'date_start',
    'date_end',
    'frequentation',
    'participant_count',
    'elevation_min',
    'elevation_max',
    'elevation_access',
    'height_diff_up',
    'height_diff_down',
    'length_total',
    'partial_trip',
    'public_transport',
    'access_condition',
    'lift_status',
    'condition_rating',
    'hut_status',
    'quality'
]
DEFAULT_REQUIRED = [
    'locales',
    'locales.title',
    'activities',
    'date_start',
    'date_end'
]
DEFAULT_LISTING = [
    'locales.title',
    'locales.summary',
    'geometry.geom',
    'activities',
    'date_start',
    'date_end',
    'elevation_max',
    'height_diff_up',
    'condition_rating',
    'quality'
]
DEFAULT_ATTRIBUTES_SETTINGS = {
    'fields': DEFAULT_FIELDS,
    'required': DEFAULT_REQUIRED,
    'listing': DEFAULT_LISTING
}

fields_outing = {
    'skitouring': {
        'fields': DEFAULT_FIELDS + [
            'elevation_up_snow',
            'elevation_down_snow',
            'snow_quantity',
            'snow_quality',
            'glacier_rating',
            'avalanche_signs',
            'locales.avalanches',
        ],
        'required': DEFAULT_REQUIRED,
        'listing': DEFAULT_LISTING
    },
    'snow_ice_mixed': {
        'fields': DEFAULT_FIELDS + [
            'elevation_up_snow',
            'elevation_down_snow',
            'snow_quantity',
            'snow_quality',
            'glacier_rating',
            'avalanche_signs',
            'locales.avalanches',
        ],
        'required': DEFAULT_REQUIRED,
        'listing': DEFAULT_LISTING
    },
    'mountain_climbing': {
        'fields': DEFAULT_FIELDS + [
            'elevation_up_snow',
            'elevation_down_snow',
            'snow_quantity',
            'snow_quality',
            'glacier_rating',
        ],
        'required': DEFAULT_REQUIRED,
        'listing': DEFAULT_LISTING
    },
    'rock_climbing': {
        'fields': DEFAULT_FIELDS,
        'required': DEFAULT_REQUIRED,
        'listing': DEFAULT_LISTING
    },
    'ice_climbing': {
        'fields': DEFAULT_FIELDS + [
            'elevation_up_snow',
            'elevation_down_snow',
            'snow_quantity',
            'snow_quality',
            'avalanche_signs',
            'locales.avalanches',
        ],
        'required': DEFAULT_REQUIRED,
        'listing': DEFAULT_LISTING
    },
    'hiking': {
        'fields': DEFAULT_FIELDS + [
        ],
        'required': DEFAULT_REQUIRED,
        'listing': DEFAULT_LISTING
    },
    'snowshoeing': {
        'fields': DEFAULT_FIELDS + [
            'elevation_up_snow',
            'elevation_down_snow',
            'snow_quantity',
            'snow_quality',
            'glacier_rating',
            'avalanche_signs',
            'locales.avalanches',
        ],
        'required': DEFAULT_REQUIRED,
        'listing': DEFAULT_LISTING
    },
    'mountain_biking': {
        'fields': DEFAULT_FIELDS + [
        ],
        'required': DEFAULT_REQUIRED,
        'listing': DEFAULT_LISTING
    },
    'via_ferrata': {
        'fields': DEFAULT_FIELDS,
        'required': DEFAULT_REQUIRED,
        'listing': DEFAULT_LISTING
    },
    'paragliding': {
        'fields': DEFAULT_FIELDS + [
        ],
        'required': DEFAULT_REQUIRED,
        'listing': DEFAULT_LISTING
    }
}
