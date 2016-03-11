# Common attributes settings used by most route activities
DEFAULT_FIELDS = [
    'locales.title',
    'locales.summary',
    'locales.description',
    'locales.gear',
    'locales.remarks',
    'locales.external_resources',
    'locales.route_history',
    'locales.title_prefix',
    'geometry.geom',
    'geometry.geom_detail',
    'activities',
    'elevation_min',
    'elevation_max',
    'height_diff_up',
    'height_diff_down',
    'height_diff_access',
    'height_diff_difficulties',
    'lift_access',
    'route_types',
    'orientations',
    'durations',
    'main_waypoint_id'
]
DEFAULT_REQUIRED = [
    'locales',
    'locales.title',
    'activities'
]
DEFAULT_LISTING = [
    'locales.title',
    'locales.title_prefix',
    'locales.summary',
    'geometry.geom',
    'elevation_max',
    'activities'
]
DEFAULT_ATTRIBUTES_SETTINGS = {
    'fields': DEFAULT_FIELDS,
    'required': DEFAULT_REQUIRED,
    'listing': DEFAULT_LISTING
}

fields_route = {
    'skitouring': {
        'fields': DEFAULT_FIELDS + [
            'locales.slope',
            'route_length',
            'glacier_gear',
            'configuration',
            'ski_rating',
            'ski_exposition',
            'labande_ski_rating',
            'labande_global_rating'
        ],
        'required': DEFAULT_REQUIRED,
        'listing': DEFAULT_LISTING
    },
    'snow_ice_mixed': {
        'fields': DEFAULT_FIELDS + [
            'locales.slope',
            'route_length',
            'difficulties_height',
            'glacier_gear',
            'configuration',
            'global_rating',
            'engagement_rating',
            'risk_rating',
            'equipment_rating',
            'ice_rating',
            'mixed_rating',
            'rock_types'
        ],
        'required': DEFAULT_REQUIRED,
        'listing': DEFAULT_LISTING
    },
    'mountain_climbing': {
        'fields': DEFAULT_FIELDS + [
            'difficulties_height',
            'glacier_gear',
            'configuration',
            'global_rating',
            'engagement_rating',
            'risk_rating',
            'equipment_rating',
            'exposition_rock_rating',
            'rock_free_rating',
            'rock_required_rating',
            'aid_rating',
            'rock_types'
        ],
        'required': DEFAULT_REQUIRED,
        'listing': DEFAULT_LISTING
    },
    'rock_climbing': {
        'fields': DEFAULT_FIELDS + [
            'difficulties_height',
            'glacier_gear',
            'configuration',
            'global_rating',
            'engagement_rating',
            'risk_rating',
            'equipment_rating',
            'exposition_rock_rating',
            'rock_free_rating',
            'rock_required_rating',
            'aid_rating',
            'rock_types',
            'climbing_outdoor_types'
        ],
        'required': DEFAULT_REQUIRED,
        'listing': DEFAULT_LISTING
    },
    'ice_climbing': {
        'fields': DEFAULT_FIELDS + [
            'locales.slope',
            'difficulties_height',
            'glacier_gear',
            'global_rating',
            'engagement_rating',
            'risk_rating',
            'equipment_rating',
            'ice_rating',
            'mixed_rating'
        ],
        'required': DEFAULT_REQUIRED,
        'listing': DEFAULT_LISTING
    },
    'hiking': {
        'fields': DEFAULT_FIELDS + [
            'route_length',
            'difficulties_height',
            'hiking_rating',
            'hiking_mtb_exposition'
        ],
        'required': DEFAULT_REQUIRED,
        'listing': DEFAULT_LISTING
    },
    'snowshoeing': {
        'fields': DEFAULT_FIELDS + [
            'locales.slope',
            'route_length',
            'difficulties_height',
            'glacier_gear',
            'configuration',
            'snowshoe_rating'
        ],
        'required': DEFAULT_REQUIRED,
        'listing': DEFAULT_LISTING
    },
    'mountain_biking': {
        'fields': DEFAULT_FIELDS + [
            'route_length',
            'difficulties_height',
            'hiking_mtb_exposition',
            'mtb_up_rating',
            'mtb_down_rating',
            'mtb_length_asphalt',
            'mtb_length_trail',
            'mtb_height_diff_portages'
        ],
        'required': DEFAULT_REQUIRED,
        'listing': DEFAULT_LISTING
    },
    'via_ferrata': {
        'fields': DEFAULT_FIELDS + [
            'route_length',
            'difficulties_height',
            'configuration',
            'engagement_rating',
            'equipment_rating',
            'via_ferrata_rating',
            'rock_types'
        ],
        'required': DEFAULT_REQUIRED,
        'listing': DEFAULT_LISTING
    }
}
