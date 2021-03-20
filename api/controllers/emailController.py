from common.email_handler.email_handler import Send_Email
from os import environ as env
from flask_restful import Resource
from common.flask_ease.request_validation import validate_request


class Email_sending(Resource):
    def post(self):
        try:
            email_obj = Send_Email(env["U_EMAIL"], env["U_PASSWORD"])
            det = validate_request('to', 'subject', 'message')
            email_content = {
                'Subject': det['subject'],
                'To': det['to'],
                'Message': det['message']
            }
            result = email_obj.send_email_gmail(message_content=email_content)
            return {"status": True, "type": "email_g", "data": f"{result}"}
        except Exception as er:
            return {"status": False, "type": "email_g", "data": f"{er}"}
