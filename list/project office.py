# 八位老师随机分配到三个办公室

import random

teacher = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
office = [[], [], []]

for name in teacher:
    num = random.randint(0, 2)
    office[num].append(name)

print(office)
i = 1

for office_name in office:
    print("办公室%d人数为%d,老师分别是:" % (i, len(office_name)))
    for name in office_name:
        print(name, end=' ')
    print('\n')
    i += 1
