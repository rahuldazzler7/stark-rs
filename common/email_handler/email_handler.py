import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


class Send_Email:
    def __init__(self, u_email: str, u_password: str):
        self.smtp_connection = smtplib.SMTP('smtp.gmail.com', 587)
        self.smtp_connection.starttls()
        self.u_email = u_email
        self.u_password = u_password
        self.smtp_connection.login(u_email, u_password)

    def send_email_gmail(self, message_content: dict) -> str:
        try:
            if message_content:
                message = message_content["Message"]
                msg = MIMEMultipart()
                msg['Subject'] = message_content["Subject"]
                msg['From'] = self.u_email
                msg['To'] = message_content["To"]
                msg.attach(MIMEText(message, 'plain'))
                self.smtp_connection.send_message(msg)
                self.smtp_connection.quit()
                return "Email Sent"
        except Exception as error:
            return f"{error}"