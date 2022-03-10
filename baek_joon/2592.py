# 2022_03_10_1
# 대표값
# 최빈값이 둘 이상일 경우 둘 중 아무거나 출력
num = {}
total = 0
for _ in range(10):
    n = int(input())
    if n not in num:
        num[n] = 0 # 초기값 선언
    num[n] += 1 
    total += n
print(num)
print(int(total/10))
print(sorted(num.items(), key=lambda x: -x[1]))
print(sorted(num.items(), key=lambda x: -x[1])[0][0]) # 카운트하여 최빈값 내림차순으로 정렬 후 최빈값 출력 
# key 대신 key=itemgetter(1)같은것 사용, 역순은 reverse=True로

# 카운터 함수 사용법
# from collections import Counter
# num = []
# for _ in range(10):
#     num.append(int(input()))
# cnt_num = Counter(num)
# # Counter의 most_common(n) 메쏘드는 등장한 횟수를 내림차순으로 정리(n개까지, 없으면 전체)
# print(sum(num)/10)
# print(cnt_num.most_common()[0][1])