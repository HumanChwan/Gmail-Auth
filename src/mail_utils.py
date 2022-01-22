from typing import List, Optional
from dict_types import Message, Payload, MessageReadable
from utils import parse_payload


class Email:
    def __init__(self, service):
        self._service = service
        self._users = self._service.users()
        self._messages = self._users.messages()
        self.userId = "me"

    def get_mail_content(self, count: int, q: Optional[str] = None) -> List[MessageReadable]:
        response = self._messages.list(userId=self.userId, maxResults=count, q=q).execute()
        message_id = [message['id'] for message in response['messages']]

        messages: List[Message] = [self._messages.get(userId=self.userId, id=m_id).execute() for m_id in message_id]
        payloads: List[Payload] = [x['payload'] for x in messages]

        messages: List[MessageReadable] = [parse_payload(payload) for payload in payloads]
        return messages

    def send_mail(self, message):
        message_out = self._messages.send(userId=self.userId, body=message).execute()
        print(f"Message id: {message_out['id']}")
        return message_out
