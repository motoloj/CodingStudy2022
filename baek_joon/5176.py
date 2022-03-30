# 2022_03_30_1
# 대회 자리
# p = 사람 수 , m = 자리 수
# 1 ≤ P, M ≤ 500) 다음 P개 줄에는 각 참가자가 원하는 자리가 주어진다. 자리는 1번부터 M번까지
for _ in range(int(input())):
    p, m = map(int, input().split())
    count = 0
    # seat = [0]*(p+1) # p가 아닌 m으로 설정, 사람p가 1, 의자가 m이 4일경우
    # , p기준으로 리스트를 만들면 리스트 인덱스 1까지 생성, 이 후 2번째 이상의 의자 호출 시 인덱스 초과로 인덱스 에러 생성
    seat = [0]*(m+1)
    for _ in range(p):
        num = int(input())
        seat[num] += 1
        if seat[num] > 1:
            count += 1
    print(count)
    # 아래 방법과 메모리, 시간 같음

# 다른방안: 입력받은 의자위치의 사람이 0일때 1로 바꾸고 0이 아닐때부터 카운트
# k = int(input())
# for _ in range(k) :
#   p, m = map(int, input().split())
#   data = [0] * (m + 1)
#   count = 0

#   for _ in range(p) :
#     value = int(input())
#     if data[value] == 0 :
#       data[value] = 1
#     else :
#       count += 1

#   print(count)