from http.client import HTTPResponse

import os.path
from googleapiclient.errors import HttpError
from googleapiclient.discovery import build, Resource
from google_auth_oauthlib.flow import InstalledAppFlow
from google.oauth2.credentials import Credentials
from google.auth.transport.requests import Request


SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']


def config():
    credentials = None
    if os.path.exists('token.json'):
        credentials = Credentials.from_authorized_user_file(
            '../token.json', SCOPES)
    if not credentials or not credentials.valid:
        if credentials and credentials.expired and credentials.refresh_token:
            credentials.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                '../credentials.json', SCOPES)
            credentials = flow.run_local_server(port=8080)
        with open('../token.json', 'w') as token:
            token.write(credentials.to_json())

    try:
        service: Resource = build('gmail', 'v1', credentials=credentials)
        return service

    except HttpError as error:
        # TODO(developer) - Handle errors from gmail API.
        print(f'An error occurred: {error}')
