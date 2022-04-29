# 2022_04_29_1
# 전자레인지
# 메모리 30840 KB 시간 68 ms
time = int(input())
five_min, one_min, ten_sec = 0, 0, 0
while time > 0:
    if time % 10 > 0:
        print(-1)
        break
    if time >= 300:
        five_min += time // 300
        time = time % 300
    elif time >= 60:
        one_min += time // 60
        time = time % 60
    else:
        ten_sec += time // 10
        time = time % 10
    
if time == 0:
    print(five_min, one_min, ten_sec)   
#--------------------------------------------- 최적화? 굳이 while 이랑 일부 조건문 안써도 될듯
# 그리디식?
# 메모리 30840 KB 시간 68 ms, 동일, 파이썬이라 별 차이가 없는 것 같다.
time = int(input())
five_min, one_min, ten_sec = 0, 0, 0

five_min += time // 300
time = time % 300
one_min += time // 60
time = time % 60
ten_sec += time // 10
if time % 10 > 0:
    print(-1)
else:
    print(five_min, one_min, ten_sec)