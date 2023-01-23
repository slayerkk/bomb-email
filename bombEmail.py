import smtplib
import email.message
print('')
#email
def enviar_email():
    corpo_email = f'coloque o corpo do email'
    
 
    msg = email.message.Message()
    msg['Subject'] = 'coloque o titulo do email'
    msg['From'] = 'coloque o seu email'
    msg['To'] = 'coloque o email alvo'
    password = 'coloque a senha de email'


#caso voce nao saiba como ativar a senha de apps, veja este video:
#https://youtu.be/6o_f_-YMhaU

    msg.add_header ('Content-Type', 'text/html')
    msg.set_payload(corpo_email )
#login
    s = smtplib.SMTP('smtp.gmail.com: 587')
    s.starttls()
    # Login Credentials for sending the mail
    s.login(msg['From'], password)
    s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
    print('o numero sera banido em breve.')

enviar_email()