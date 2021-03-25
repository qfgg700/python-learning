str1 = 'Jimmy'

for i in str1:
    if i == 'm':
        print()
        print('jump m and skip out')
        continue
    print(i, end='\t')
else:
    print('successfully output')
