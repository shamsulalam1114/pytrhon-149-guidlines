m = "akash's world"
n = "asim\'s world"

print(m[0:7])
print(m[8:])
print(len(m))
print(m[0])
print(n)
print(m.lower())
print(n.upper())
print(m.count('a'))
print(m.count('world'))
print(n.find('asim'))
print(n.find('ball'))
print(n.find('i'))
print(n.replace('world','universe'))

greetings= 'hello'
name= 'michle'
message = greetings + ', '+ name + ', '+ ' welcome to my world'
print(message)


greetings= 'hello'
name= 'akash'
message = '{}, {}.welcome!'.format(greetings , name)
print(message)

message = f'{greetings}, {name.upper()}.welcome!'
print(dir(message))
print(help(str))
