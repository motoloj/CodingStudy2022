# 2022_02_18_3
# X보다 작은 수
n, x = map(int, input().split())
stack = '' 
number = map(int, input().split())
for i in number:
    if i < x:
        stack += (str(i) +" ") 
        # print(i, end=" ")
        # end의 출력 마지막에 들어오는 내용 기본 값은 \n이기 때문에 다른 값으로 바꾸면 한 줄씩이 아닌 이어서 출력
        # a,b => 한칸씩 띄어쓰기로 출력, sep=""옵션은 출력물들 사이의 내용들을 수정가능, 기본 값은 공백
print(stack.rstrip())
