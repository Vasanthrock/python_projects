import smtplib
import os
from twilio.rest import Client
account_sid = os.getenv("account_sid")
auth_token = os.getenv("auth_token")


class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    def __init__(self):
        # Retrieve environment variables only once
        self.smtp_address = os.getenv("smtp_address")
        self.email = os.getenv("email")
        self.email_password = os.getenv("email_password")
        self.twilio_virtual_number = os.getenv("twilio_virtual_number")
        self.twilio_verified_number = os.getenv("twilio_verified_number")
        self.whatsapp_number = os.getenv("whatsapp_number")
        # Set up Twilio Client and SMTP connection
        self.client = Client(account_sid, auth_token)
        self.connection = smtplib.SMTP(self.smtp_address)

    def send_sms(self, message_body):
        """
        Sends an SMS message through the Twilio API.
        This function takes a message body as input and uses the Twilio API to send an SMS from
        a predefined virtual number (provided by Twilio) to your own "verified" number.
        It logs the unique SID (Session ID) of the message, which can be used to
        verify that the message was sent successfully.

        Parameters:
        message_body (str): The text content of the SMS message to be sent.

        Returns:
        None

        Notes:
        - Ensure that `TWILIO_VIRTUAL_NUMBER` and `TWILIO_VERIFIED_NUMBER` are correctly set up in
        your environment (.env file) and correspond with numbers registered and verified in your
        Twilio account.
        - The Twilio client (`self.client`) should be initialized and authenticated with your
        Twilio account credentials prior to using this function when the Notification Manager gets
        initialized.
        """
        message = self.client.messages.create(
            from_=self.twilio_virtual_number,
            body=message_body,
            to=self.twilio_verified_number
        )
        # Prints if successfully sent.
        print(message.sid)

        # Is SMS not working for you or prefer whatsapp? Connect to the WhatsApp Sandbox!
        # https://console.twilio.com/us1/develop/sms/try-it-out/whatsapp-learn

    def send_whatsapp(self, message_body):
        message = self.client.messages.create(
            from_=f'whatsapp:{self.whatsapp_number}',
            body=message_body,
            to=f'whatsapp:{self.twilio_verified_number}'
        )
        print(message.sid)

    def send_emails(self, email_list, email_body):
        with self.connection:
            self.connection.starttls()
            self.connection.login(self.email, self.email_password)
            for email in email_list:
                self.connection.sendmail(
                    from_addr=self.email,
                    to_addrs=email,
                    msg=f"Subject:New Low Price Flight!\n\n{email_body}".encode('utf-8')
                )

        # Send email using the smtplib module.

    def send_mail(self, message_body):
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()  # Secure the connection
            server.login(self.email, self.email_password)
            server.sendmail(
                from_addr=self.email,
                to_addrs= os.getenv("to_addrs"),
                msg=f"Subject:Flight Deals\n\n{message_body}"
            )
            print("Email sent successfully!")