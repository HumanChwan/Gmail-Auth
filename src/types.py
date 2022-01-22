from typing import TypedDict, Literal


class MessageReadable(TypedDict):
    From: str
    To: str
    Subject: str
    text: str
    html: str


MessageReadableKeys = Literal['From', 'To', 'Subject', 'text', 'html']
