str1 = 'hello world and hello python and send for Jimmy'

# find，找不到返回-1
print(str1.find('Jimmy'))
print(str1.find('and'))
print(str1.find('and', 14, 40))
print(str1.find('666'))

# index，找不到报错
print(str1.index('Jimmy'))
print(str1.index('and'))
print(str1.index('and', 14, 40))
# print(str1.index('666'))

# count
print(str1.count('and'))
print(str1.count('l', 3, 10))
print(str1.count('ands'))

# rfind,rindex从右侧开始
