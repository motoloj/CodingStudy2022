# 2022_03_12_1
# UCPC는 무엇의 약자일까?

s = list(input())
count = 0
for i in s:
    if i == 'U' and count == 0:
        count = 1 
    if i == 'C' and count == 1:
        count = 2
    if i == 'P' and count == 2:
        count = 3
    if i == 'C' and count== 3:
        count = 4
        break
if count == 4:
    print("I love UCPC")
else:
    print('I hate UCPC')