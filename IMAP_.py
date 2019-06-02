import imaplib, imapclient
import pyzmail
import pprint

imaplib._MAXLINE = 10_000_000
imapObj = imapclient.IMAPClient('imap.yandex.ru', ssl=False)
imapObj.login('ostap666@yandex.ru', 'wzf3v42lForeMan*-17404')
# pprint.pprint(imapObj.list_folders())
imapObj.select_folder('INBOX', readonly=True) #False if want to check read mail

# UIDs = imapObj.search(['SINCE', '01-Feb-2019', 'BEFORE', '20-Feb-2019'])
# UIDs = imapObj.search(['SINCE', '01-Dec-2018', 'FROM', 'Vyacheslav.Volkov@nmtport.ru'])
UIDs = imapObj.search('UNSEEN')
print(UIDs)

raw_msg = imapObj.fetch(UIDs, ['BODY[]'])
ms = raw_msg[0]
mail = pyzmail.PyzMessage.factory(raw_msg[UIDs[0]] [b'BODY[]'])

print(mail.get_address('from'))
print(mail.get_subject())
messege = mail.text_part.get_payload().decode(mail.text_part.charset)
print(messege)
# ========DEL MSG======
imapObj.delete_messages(UIDs[0])
imapObj.expunge()




imapObj.logout()


