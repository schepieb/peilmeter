# Importeer de smtplib voor email functies.
import smtplib
 
# Importeer de email modules.
from email.mime.text import MIMEText
 
def stuurbericht():

    # Definieer email adressen.
    adres_naar = 'xxx@gmail.com'
    adres_van = 'xxx@telenet.be'
 
    # Definieer SMTP email server gegevens.
    smtp_server = 'smtp.telenet.be'
    smtp_gebruiker = 'xxx@telenet.be'
    smtp_wachtwoord = 'xxx'
    smtp_poort = 587
 
    # Bouw de email op.
    msg = MIMEText('This is a test email')
    msg['To'] = adres_naar
    msg['From'] = adres_van
    msg['Subject'] = 'Put bijna leeg !'
 
    # Stuur het bericht via de SMTP server.
    s = smtplib.SMTP_SSL(smtp_server)
    s.login(smtp_gebruiker, smtp_wachtwoord)
    print("test")
    s.sendmail(adres_van, adres_naar, msg.as_string())
    s.quit()
    
stuurbericht()