str1 = 'Jimmy'

for i in str1:
    if i == 'm':
        print('jump m and skip out')
        break
    print(i, end='\t')
else:
    print('successfully output')
