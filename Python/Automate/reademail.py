import imapclient
# import pyzmail
conn = imapclient.IMAPClient('imap.gmail.com',ssl=True)

user = 'asdfsdfasdf552@gmail.com'
password = 'pGGqjGXeYuBnFU5'
conn.login(user,password)

conn.select_folder('INBOX',readonly=True)

UIDs = conn.search(['FROM', 'juniorgutierrez2000py@gmail.com'])

print(UIDs)
conn.logout()

'''
rawMessage = conn.fetch(UIDs[0],['BODY','FLAGS'])
message = pyzmail.PyzMessage.factory(rawMessage[UIDs[0]][b'BODY[]'])
print(message.get_subject())
print(message.get_addresses('from'))
# pyzmail dont work
'''