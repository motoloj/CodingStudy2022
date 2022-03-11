# 2022_03_09_2
# 보물
n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
a = sorted(a)
b = sorted(b, reverse=True)
result = 0
for i in range(n):
    result += a[i]*b[i]
print(result)

# b 리스트 재배열  X 조건 => b의 최대값을 뽑아 곱해줌
# >>>>>>>>>>>> b의 최대값의 인덱스순서대로 a를 재정렬
n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
new_a = [0]*n
result = 0
a = sorted(a, reverse=True)
for _ in range(n):
    max_index = b.index(max(b))
    new_a[max_index] = a[max_index]
    result += new_a[max_index] * b[max_index]
    b[max_index] = -1
print(result)

# pop사용 (변수 선언, 입력 동일, a리스트 정렬은 하지않고 포문내부만 다름)
for _ in range(n):
    result += a.pop(a.index(min(a)) * b.pop(b.index(max(b))))
# pop은 인자가 없을시 가장끝 부분 pop시킨걸 반환