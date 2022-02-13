# 2022-02-13_1
from datetime import datetime

student_num = int(input())
name_list = []
birth_list = []

for _ in range(student_num):
    name, day, month, year = input().split( )
    name_list.append(name)
    birth = year + "-" + month + "-" + day
    birth = datetime.strptime(birth, "%Y-%m-%d").date()
    birth_list.append(birth)

# datetime 포맷으로 바꾼 생일이 최솟값이면 나이 많음, 최대값이면 나이 적음
younger = max(birth_list)
older = min(birth_list)

# 첫 줄: 나이 적은 사람 출력
print(name_list[birth_list.index(younger)])

# 둘째 줄: 나이 많은 사람 출력
print(name_list[birth_list.index(older)])