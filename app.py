from gmailauth import Email


def main():
    email_service = Email('dinesss169@gmail.com')

    to = 'dinesss169@gmail.com'
    subject = 'kwargs testing'
    text = 'pls help me!'
    html = '<strong style="color: red">pls help me!</strong>'

    mail = email_service.create_mail(to=to, subject=subject, text=text, html=html)
    email_service.send_mail(mail)
    print(email_service)


if __name__ == '__main__':
    main()
