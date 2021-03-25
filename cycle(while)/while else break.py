i = 0

while i < 6:
    if i == 4:
        break
    print(i, end='\t')
    i += 1
else:
    print('successfully output')
# break没有跑完循环，所以不会进入到else
