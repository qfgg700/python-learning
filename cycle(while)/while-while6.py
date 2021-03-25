i = 6
j = 0
k = 0

while i > 0:
    while j < i:
        while k < 6 - i:
            print(' ', end=' ')
            k += 1
        print('*', end=' ')
        j += 1
    print()
    i -= 1
    j = 0
    k = 0
