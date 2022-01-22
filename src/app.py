from config import config
from typing import List
from dict_types import MessageReadable
from mail_utils import Email
from utils import print_message, create_mail


def main():
    service = config()
    email_service = Email(service)
    messages: List[MessageReadable] = email_service.get_mail_content(1)
    for index, message in enumerate(messages):
        print_message(message, index)

    mail = create_mail('dineshchukkala169@gmail.com', 'Dinesh Chukkala <dinesss169@gmail.com>',
                       'Test 1', "Bhai bhai Kya haal hai baaki")
    email_service.send_mail(mail)


if __name__ == '__main__':
    main()
