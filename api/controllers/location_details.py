from flask_restful import Resource
from common.location.location_handler import Location_details, find_nearest_locations, get_place
from common.flask_ease.request_validation import validate_request


class Location_Search(Resource):
    def post(self):
        pass


class Where_am_I(Resource):
    def post(self):
        loc_obj = Location_details()
        my_loc = loc_obj.get_my_coordinates()
        me = get_place(my_loc["latitude"], my_loc["longitude"])
        return {"status": True, "type": "where_am_i", "data": me["place"]}


class Location_distance(Resource):
    def post(self):
        pass


class Location_near_me(Resource):
    def post(self):
        vr = validate_request("query")
        res = find_nearest_locations(vr["query"])
        return {"status": True, "type": "location_near_me", "data": res["message"]}
