str1 = 'hello world and hello python and send for jimmy'

print(str1.startswith('hello'))
print(str1.startswith('orld', 7, 40))
print(str1.startswith('world', 7, 40))

print(str1.endswith('jimmy'))
print(str1.endswith('o', 0, 4))
print(str1.endswith('o', 0, 5))
