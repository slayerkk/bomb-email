import smtplib
import email.message

#email
def enviar_email():
    corpo_email = 'teste'
    
 
    msg = email.message.Message()
    msg['Subject'] = 'teste'
    msg['From'] = 'slayerlindo6@gmail.com'
    msg['To'] = 'maneosorio55@gmail.com'
    password = 'qzqfmxnlxaplzbbs'
    msg.add_header ('Content-Type', 'text/html')
    msg.set_payload(corpo_email )
#login
    s = smtplib.SMTP('smtp.gmail.com: 587')
    s.starttls()
    # Login Credentials for sending the mail
    s.login(msg['From'], password)
    s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
    print('nuked.')

enviar_email()