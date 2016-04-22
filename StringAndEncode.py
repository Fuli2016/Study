#小明的成绩从去年的72分提升到了今年的85分，请计算小明成绩提升的百分点，并用字符串格式化显示出'xx.x%'，只保留小数点后1位：
last=72.0
score=85.0
percent=(score-last)*100/score
print(percent)
print(('%.1f %%') % percent)
