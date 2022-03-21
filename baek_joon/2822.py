# 2022_03_21_1
# 점수 계산
# 1. max 값 pop후 값으로 인덱스 위치, OR 2. 정렬후 위치 순서대로 index출력
num = [int(input()) for _ in range(8) ]
sort_num = sorted(num, reverse=True)
print(sum(sort_num[:5]))
lst = sorted([(num.index(i) + 1) for i in sort_num[:5]])
# unpack 사용
print(*lst, sep=" ")