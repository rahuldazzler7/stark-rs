import datetime
from flask_restful import Resource


class Date_time(Resource):
    def post(self):
        try:
            datetime_object = datetime.datetime.now()
            return {"status": True, "type": "date_time", "data": f"{datetime_object}"}
        except Exception as er:
            return {"status": False, "type": "date_time", "data": f"{er}"}


class Date_t(Resource):
    def post(self):
        try:
            date_object = datetime.date.today()
            return {"status": True, "type": "date", "data": f"{date_object}"}
        except Exception as er:
            return {"status": False, "type": "date", "data": f"{er}"}


class Time_t(Resource):
    def post(self):
        try:
            now = datetime.datetime.now().time()
            current_time = now.strftime("%H:%M:%S")
            return {"status": True, "type": "time", "data": f"{current_time}"}
        except Exception as er:
            return {"status": False, "type": "time",  "data": f"{er}"}

