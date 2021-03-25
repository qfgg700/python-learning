import random

player = input('player：')
computer = random.randint(1,3)

if player == '石头':
    a = 1
elif player == '剪刀':
    a = 2
else:
    a = 3

if computer == 1:
    print('石头')
elif computer == 2:
    print('剪刀')
else:
    print('布')

b = computer

if a == b:
    print('平局')
else:
    c = a - b
    if c == -1:
        print('player win')
    elif c == 2:
        print('player win')
    elif c == -2:
        print('computer win')
    elif c == 1:
        print('computer win')
    else:
        print('fatal error')
