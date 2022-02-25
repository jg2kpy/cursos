spam = ['cat','bat','rat','elephant']

print(spam)
print(spam[0])

print(spam[-1])
print(spam[-2])

#Slice
print(spam[1:3])
print(spam[:3])
print(spam[1:])

del spam[2]
print(spam)

print(len("Hello"))
print(len(spam))

print(list("Hello"))

a = "AAA"
b = "BBB"

a, b = b, a

print(a)
print(b)

spam.append('moose')
spam.insert(1,'chicken')

print(spam)

spam.sort(reverse=True)

print(spam)

spam.sort(key=str.lower)

print(spam)