i = 1
j = 1

while i < 10:
    while j < (i + 1):
        c = i * j
        print('%d*%d=%d' % (i, j, c), end='\t')
        j += 1
    print()
    i += 1
    j = 1
