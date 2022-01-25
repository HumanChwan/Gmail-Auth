from typing import TypedDict, Literal, List, Optional, Any


class MessageReadable(TypedDict):
    From: str
    To: str
    Subject: str
    text: str
    html: str


MessageReadableKeys = Literal['From', 'To', 'Subject', 'text', 'html']


class Body(TypedDict):
    data: Optional[str]
    attachmentId: Optional[str]
    size: int


class Header(TypedDict):
    name: str
    value: str


class Payload(TypedDict):
    body: Body
    mimeType: str
    partId: str
    filename: Optional[str]
    headers: List[Header]
    parts: Any


class Message(TypedDict):
    internalDate: str
    historyId: str
    payload: Payload
    snippet: str
    raw: str
    threadId: str
    labelIds: List[str]
    id: str
