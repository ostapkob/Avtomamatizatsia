import smtplib

smtpObj = smtplib.SMTP_SSL('smtp.yandex.ru', 465)
print(type(smtpObj))
smtpObj.ehlo()
smtpObj.login('ostap666@yandex.ru', 'wF*-17')
BODY = "\r\n".join((
    "From: %s" % FROM,
    "To: %s" % TO,
    "Subject: %s" % SUBJECT ,
    "",
    text
))

smtpObj.sendmail('ostap666@yandex.ru', 'disp.smen@nmtport.ru', 'Subject: Soro \nHellow Ostapiiiiiiiiiiiiiiiiiiiiii')


smtpObj.quit()








