from common.stark_eye.mask_detection import decison_make
from common.stark_eye.human_face_detection import human_face_detector
from flask_restful import Resource
from os import environ as env


class Mask_Detector(Resource):
    def post(self):
        try:
            decison_make(env['prototxtPath'], env['weightsPath'], env['maskmodelPath'])
            return {"status": True, "type": "mask_detector", "data": f"Result detected successfully"}
        except Exception as err:
            return {"status": False, "type": "mask_detector", "data": f"{err}"}


class Face_Detector(Resource):
    def post(self):
        try:
            human_face_detector(env['prototxtPath'], env['weightsPath'])
            return {"status": True, "type": "face_detector", "data": f"Result detected successfully"}
        except Exception as err:
            return {"status": False, "type": "face_detector", "data": f"{err}"}
