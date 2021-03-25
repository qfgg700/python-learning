# 1
num1 = 1
str1 = '10.12'
print(type(float(num1)))
print(type(float(str1)))
print(float(num1))
print(float(str1))

# 2
print(type(str(num1)))

# 3
list1 = [10, 20, 30]
print(tuple(list1))  # 转元组

# 4
t1 = (100, 200, 300)
print(list(t1))

# 5 eval()
# 字符串里面什么样就转成什么类型
str2 = '1'
str3 = '1.01'
str4 = '(2, 3, 4)'
str5 = '[6, 7, 8]'

print(type(eval(str2)))
print(type(eval(str3)))
print(type(eval(str4)))
print(type(eval(str5)))
