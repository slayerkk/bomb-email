import smtplib
import email.message

#email
def enviar_email():
    corpo_email = 'teste'
    
    msg = email.message.Message()
    msg['Subject'] = 'titulo do email'
    msg['From'] = 'coloque o email que voce usara para atacar'
    msg['To'] = 'coloque o email de qm vc qr atacar'
    password = 'sua senha de app para email'
    msg.add_header ('Content-Type', 'text/html')
    msg.set_payload(corpo_email )

#video tuto p qm nn sabe criar senha de app
#https://youtu.be/6o_f_-YMhaU

#login
    s = smtplib.SMTP('smtp.gmail.com: 587')
    s.starttls()
    # Login Credentials for sending the mail
    s.login(msg['From'], password)
    s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
    print('\033[1;31mEMAIL ENVIADO')

enviar_email()