# 2022_03_02_1
# 약수 구하기
n, k = map(int, input().split())
count = 0
for i in range(1, n+1):
    if n % i == 0:
        count +=1
    if count == k:
        break
    if i >= n and count < k:
        i = 0
        break
print(i) # 조건 잘못 설정시 포문이 끝까지 돌아 i가 최대 범위로 반환
# 배열(리스트)에 모든 약수를 저장하고 k가 리스트 길이보다 크면 0반환하는 방법도 있다. 