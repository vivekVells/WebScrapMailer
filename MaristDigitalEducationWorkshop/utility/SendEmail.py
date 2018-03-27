import smtplib

def send_email(sender, password, receiver, subject, body):
    sent_from = sender
    to = [receiver]
    subject = subject

    body = body

    email_text = """\ 
    From: %s  
    To: %s  
    Subject: %s

    %s
    
    Thanks & regards,
    Digitial Education Representative
    Marist College
    XXXX-XXX-XXX
    """ % (sent_from, ", ".join(to), subject, body)

    try:
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        # server = smtplib.SMTP_SSL('smtp.elasticemail.com', 2525)
        server.ehlo()
        server.login(sender, password)
        server.sendmail(sent_from, to, email_text)
        server.close()

        print('Email sent!')
    except:
        print('Something went wrong...')