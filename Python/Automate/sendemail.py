import smtplib

conn = smtplib.SMTP('smtp.gmail.com', 587)
conn.ehlo()
conn.starttls()

user = 'asdfsdfasdf552@gmail.com'
password = 'pGGqjGXeYuBnFU5'
print('Status code: ' + str(conn.login(user,password)[0]))

message = "Subject: So long...4\n\nHello4\n\n"
to_addrs = 'kikice8676@ehstock.com'
conn.sendmail(user, to_addrs, message)

print('Email sended')

conn.quit()