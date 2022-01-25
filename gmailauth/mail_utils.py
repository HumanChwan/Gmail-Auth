import base64
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from typing import List, Optional

from .utils import parse_payload
from .config import config
from .dict_types import Message, Payload, MessageReadable


class Email:
    """
            Class Email\n
            ------------
            Initialize Email class object as:
            \n
            ``email_service = Email("email@email.com")``
            methods:
                get_email_content\n
                create_mail\n
                send_mail
            Args
            ----------
            @sender: str (sender email address)
        """
    def __init__(self, sender: str):
        self._service = config()
        self._users = self._service.users()
        self._messages = self._users.messages()

        self.userId = "me"
        self.sender = sender

    def get_mail_content(self, count: int, q: Optional[str] = None) -> List[MessageReadable]:
        response = self._messages.list(userId=self.userId, maxResults=count, q=q).execute()
        message_id = [message['id'] for message in response['messages']]

        messages: List[Message] = [self._messages.get(userId=self.userId, id=m_id).execute() for m_id in message_id]
        payloads: List[Payload] = [x['payload'] for x in messages]

        messages: List[MessageReadable] = [parse_payload(payload) for payload in payloads]
        return messages

    def create_mail(self, **kwargs: str) -> object:
        to = kwargs['to']
        subject = kwargs['subject']
        text = kwargs['text']
        html = kwargs['html']

        message = MIMEMultipart('alternative')

        text_part = MIMEText(text, 'text')
        html_part = MIMEText(html, 'html')

        message['to'] = to
        message['from'] = self.sender
        message['subject'] = subject

        message.attach(text_part)
        message.attach(html_part)

        return {'raw': base64.urlsafe_b64encode(bytes(message.as_string(), 'utf-8')).decode('utf-8')}

    def send_mail(self, message):
        message_out = self._messages.send(userId=self.userId, body=message).execute()
        print(f"Message id: {message_out['id']}")
        return message_out

    def __str__(self):
        return str({'sender': self.sender})
