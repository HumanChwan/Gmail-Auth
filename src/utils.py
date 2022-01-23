import base64
from typing import List

from dict_types import MessageReadable, Payload, Body, MessageReadableKeys


def readable(x: str) -> str:
    return base64.urlsafe_b64decode(x).decode('utf-8')


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


def print_message(message: MessageReadable, index: int = 0):
    print(f"Message {index + 1}\nFROM: {message['From']}\nTO: {message['To']}\nSUBJECT: {message['Subject']}"
          f"\nTEXT:\n{message['text']}\nHTML: {message['html']}\n\n")
