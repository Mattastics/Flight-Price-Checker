from twilio.rest import Client
import smtplib
import requests
TWILIO_SID = "*****************************"
TWILIO_AUTH_TOKEN = "******************************"
TWILIO_VIRTUAL_NUMBER = "***********"
TWILIO_VERIFIED_NUMBER = "***********"

my_email = "****************"
my_password = "*******************"

sheety_users = "https://api.sheety.co/aba2ece9aa1a17eb62a8b40e0be55b8b/flightDeals/users/"


class NotificationManager:

    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=TWILIO_VIRTUAL_NUMBER,
            to=TWILIO_VERIFIED_NUMBER,
        )
        print(message.sid)




    def send_emails(self, emails, message, google_flight_link):
        with smtplib.SMTP(EMAIL_PROVIDER_SMTP_ADDRESS) as connection:
            connection.starttls()
            connection.login(MY_EMAIL, MY_PASSWORD)
            for email in emails:
                connection.sendmail(
                    from_addr=MY_EMAIL,
                    to_addrs=email,
                    msg=f"Subject:New Low Price Flight!\n\n{message}\n{google_flight_link}".encode('utf-8')
                )
