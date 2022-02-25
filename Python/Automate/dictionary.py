import pprint

myCat = {
    'size': 'fat',
    'color': 'gray',
    'disposition': 'loud'
}

print('My cat has ' + myCat['color'] + 'color')

print(myCat.keys())
print(list(myCat.keys()))
print(myCat.values())
print(myCat.items())

print(myCat.get('age',-1))

message = 'It was a bright cold day in April'

count = {}
for caracter in message:
    count.setdefault(caracter, 0)
    count[caracter] = count[caracter] + 1

pprint.pprint(count)

text = pprint.pformat(count)
print('\n')
print(text)

cat = {'name': 'Michi', 'age': 4, 'color': 'black and white'}
print (type(cat))