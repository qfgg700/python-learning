money = int(input('money='))
seat = int(input('seat='))

if money > 0:
    if seat > 0:
        print('坐票')
    else:
        print('站票')
else:
    print('no money')
