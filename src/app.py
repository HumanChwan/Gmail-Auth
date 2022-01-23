from config import config
from mail_utils import Email


def main():
    service = config()
    email_service = Email(service, 'dinesss169@gmail.com')

    to = 'dinesss169@gmail.com'
    subject = 'kwargs testing'
    text = 'pls help me!'
    html = '<strong style="color: red">pls help me!</strong>'

    # mail = email_service.create_mail(to=to, subject=subject, text=text, html=html)
    # email_service.send_mail(mail)
    print(email_service)


if __name__ == '__main__':
    main()
