import os
import base64
from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials
from google.oauth2 import service_account


delegated_creds = process.credentials
# Create a Gmail API service client
service = build('gmail', 'v1', credentials=delegated_creds)

# Email content
sender_email = 'jacqueline.escalante@bairesdev.com'
recipient_email = 'jacqueline.escalante@bairesdev.com'
subject = 'Test'
message_text = 'This is the body of the email.'

message = f"From: {sender_email}\nTo: {recipient_email}\nSubject: {subject}\n\n{message_text}"
raw_message = base64.urlsafe_b64encode(message.encode("utf-8")).decode("utf-8")

# Send the email
service.users().messages().send(userId=sender_email, body={'raw': raw_message}).execute()
print("Email sent successfully!")