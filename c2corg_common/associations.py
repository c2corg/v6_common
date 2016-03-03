from c2corg_common.document_types import *

valid_associations = set([
    # associations with outings
    (ROUTE_TYPE, OUTING_TYPE),
    (WAYPOINT_TYPE, OUTING_TYPE),
    (USERPROFILE_TYPE, OUTING_TYPE),

    # associations with waypoints
    (WAYPOINT_TYPE, WAYPOINT_TYPE),

    # associations with routes
    (ROUTE_TYPE, ROUTE_TYPE),
    (WAYPOINT_TYPE, ROUTE_TYPE),

    # associations with images
    (IMAGE_TYPE, IMAGE_TYPE),
    (WAYPOINT_TYPE, IMAGE_TYPE),
    (OUTING_TYPE, IMAGE_TYPE),
    (ROUTE_TYPE, IMAGE_TYPE),
    (USERPROFILE_TYPE, IMAGE_TYPE),
])
