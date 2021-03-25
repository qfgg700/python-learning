i = 0

while i < 6:
    if i == 4:
        i += 1
        continue
    print(i, end='\t')
    i += 1
else:
    print('successfully output')
# continue跑完循环，所以会进入到else
