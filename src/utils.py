import base64
from email.mime.text import MIMEText
from typing import List

from dict_types import MessageReadable, Payload, Body, MessageReadableKeys


def readable(x: str) -> str:
    parsed_in_bytes = base64.urlsafe_b64decode(x)
    parsed_as_string = parsed_in_bytes.decode('utf-8')
    return parsed_as_string


def parse_payload(payload: Payload) -> MessageReadable:
    if payload['mimeType'] == 'text/plain':
        text: Body = payload['body']
        html: Body = payload['body']
    else:
        text: Body = payload['parts'][0]['body']
        html: Body = payload['parts'][1]['body']

    message: MessageReadable = {
        'From': '',
        'To': '',
        'Subject': '',
        'text': readable(text['data']),
        'html': readable(html['data'])
    }
    keys: List[MessageReadableKeys] = ['From', 'To', 'Subject']

    for header in payload['headers']:
        for header_name in keys:
            if header_name == header['name']:
                message[header_name] = header['value']
                break

    return message


def create_mail(to: str, sender: str, subject: str, message_text: str) -> object:
    message = MIMEText(message_text)
    message['to'] = to
    message['from'] = sender
    message['subject'] = subject
    return {'raw': base64.urlsafe_b64encode(bytes(message.as_string(), 'utf-8')).decode('utf-8')}


def print_message(message: MessageReadable, index: int = 0):
    print(f"Message {index + 1}\nFROM: {message['From']}\nTO: {message['To']}\nSUBJECT: {message['Subject']}"
          f"\nTEXT:\n{message['text']}\nHTML: {message['html']}\n\n")
