# 2022_04_03_1
# 짝수를 찾아라
# 시간 164ms 

# for _ in range(int(input())):
#    even =  [i for i in map(int, input().split()) if i % 2 == 0 ]
#    print(sum(even), min(even))
   
# ------------------------------ 시간 테스트
# 메모리 30860kb로 동일, 시간 160ms로 더 적음

for _ in range(int(input())):
    even = []
    num = map(int, input().split())
    for i in num:
        if i % 2 == 0:
            even.append(i)
    print(sum(even), min(even))