from config import config
from typing import List, Optional
import base64

from types import MessageReadable, MessageReadableKeys


def readable(x: str) -> str:
    parsed_in_bytes = base64.urlsafe_b64decode(x)
    parsed_as_string = parsed_in_bytes.decode('utf-8')
    return parsed_as_string


def parse_payload(payload) -> MessageReadable:
    mail_content = payload['parts']
    message: MessageReadable = {
        'From': '',
        'To': '',
        'Subject': '',
        'text': readable(mail_content[0]['body']['data']),
        'html': readable(mail_content[1]['body']['data'])
    }

    for header in payload['headers']:
        if header['name'] in ['From', 'To', 'Subject']:
            header_name: MessageReadableKeys = header['name']
            message[header_name] = header['value']

    return message


class Email:
    def __init__(self, service):
        self._service = service
        self._users = self._service.users()
        self._messages = self._users.messages()
        self.userId = "me"

    def get_mail_content(self, count: int, q: Optional[str] = None) -> List[MessageReadable]:
        response = self._messages.list(userId=self.userId, maxResults=count, q=q).execute()
        message_id = [message['id'] for message in response['messages']]

        messages = [self._messages.get(userId=self.userId, id=m_id).execute() for m_id in message_id]
        payloads = [x['payload'] for x in messages]

        messages = [parse_payload(payload) for payload in payloads]
        return messages


def main():
    service = config()
    email_service = Email(service)
    messages: List[MessageReadable] = email_service.get_mail_content(1)
    for index, message in enumerate(messages):
        print(f"Message {index + 1}\nFROM: {message['From']}\nTO: {message['To']}\nSUBJECT: {message['Subject']}"
              f"\nTEXT:\n{message['text']}\nHTML: {message['html']}\n\n")


if __name__ == '__main__':
    main()
