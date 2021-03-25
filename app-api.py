from flask import Flask
from flask_restful import Api

from api_controllers.search_queriesController import Wiki_Search, Google_search, Open_youtube
from api_controllers.dateTimeController import Date_t, Date_time, Time_t
from api_controllers.emailController import Email_sending
from api_controllers.detector import Mask_Detector, Face_Detector
from api_controllers.location_details import Where_am_I, Location_near_me


app = Flask(__name__)
api = Api(app)

api.add_resource(Wiki_Search, "/dependencies/v1/wiki_search")
api.add_resource(Google_search, "/dependencies/v1/google_search")
api.add_resource(Open_youtube, "/dependencies/v1/youtube_search")
api.add_resource(Date_time, "/dependencies/v1/date_and_time")
api.add_resource(Date_t, "/dependencies/v1/date_today")
api.add_resource(Time_t, "/dependencies/v1/time_now")
api.add_resource(Email_sending, "/dependencies/v1/send_email_gmail")
api.add_resource(Mask_Detector, "/dependencies/v1/detect_mask")
api.add_resource(Face_Detector, "/dependencies/v1/detect_face")
api.add_resource(Where_am_I, "/dependencies/v1/where_am_i")
api.add_resource(Location_near_me, "/dependencies/v1/location_near_me")

if __name__ == "__main__":
    app.run(debug=False, host='0.0.0.0', port=5001)