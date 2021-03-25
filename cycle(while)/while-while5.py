i = 0
j = 0

while i < 6:
    k = 5 - i
    while j < i+1:
        while k > 0:
            print(' ', end=' ')
            k -= 1
        print('*', end=' ')
        j += 1
    print()
    i += 1
    j = 0
