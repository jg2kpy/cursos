import requests

res = requests.get('http://juniorgutierrez.com/images/IMG_20201124_092509624.jpg')
res.raise_for_status()

print(res.status_code)

playFile = open('profile.png','wb')

for chunk in res.iter_content(100000):
    playFile.write(chunk)

playFile.close()