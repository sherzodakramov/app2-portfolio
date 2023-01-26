import smtplib, ssl


def send_email(message):
    host = "smtp.gmail.com"
    port = 465
    username = "sherzodakramov1999@gmail.com"
    password = "ysoaovjzgcaiiocs"
    receiver = "sherzodakramov1999@gmail.com"
    # It holds secure context for sending email securely
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)




