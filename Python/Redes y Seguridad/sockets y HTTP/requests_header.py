import requests

domain = input("Enter the hostname http://")

response = requests.get('http://' + domain)

print(str(response.json))

print('Status code: '+ str(response.status_code),'\n')

print('Headers response:')
for header, value in response.headers.items():
    print(f'{header}: {value}')
print('\n')

print('Headers request:')
for header, value in response.request.headers.items():
    print(f'{header}: {value}')
print('\n')