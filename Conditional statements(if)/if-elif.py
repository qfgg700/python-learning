score = int(input('输入成绩：'))

if score < 60:
    print('成绩为%d，不及格' % score)
elif (score < 90 ) and (score >= 60):
    print('成绩为%d，及格' % score)
elif (score < 100 ) and (score >= 90):
    print('成绩为%d，优秀' % score)
else:
    print('满分')
