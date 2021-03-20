from flask import Flask
from flask_restful import Api
from dotenv import load_dotenv

from controllers.search_queriesController import Wiki_Search, Google_search, Open_youtube
from controllers.dateTimeController import Date_t, Date_time, Time_t
from controllers.emailController import Email_sending
from controllers.detector import Mask_Detector, Face_Detector
from controllers.location_details import Where_am_I, Location_near_me

load_dotenv(verbose=True)


app = Flask(__name__)
api = Api(app)

api.add_resource(Wiki_Search, "/api/v1/wiki_search")
api.add_resource(Google_search, "/api/v1/google_search")
api.add_resource(Open_youtube, "/api/v1/youtube_search")
api.add_resource(Date_time, "/api/v1/date_and_time")
api.add_resource(Date_t, "/api/v1/date_today")
api.add_resource(Time_t, "/api/v1/time_now")
api.add_resource(Email_sending, "/api/v1/send_email_gmail")
api.add_resource(Mask_Detector, "/api/v1/detect_mask")
api.add_resource(Face_Detector, "/api/v1/detect_face")
api.add_resource(Where_am_I, "/api/v1/where_am_i")
api.add_resource(Location_near_me, "/api/v1/location_near_me")

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5001)