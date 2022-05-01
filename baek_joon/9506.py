# 2022_05_01_1
# 약수들의 합
while True:
    n = int(input())
    if n == -1:
        break
    m = int(n**0.5)  # 약수들의 짝이 있기 때문에 제곱근 까지 구한다, float 가능성때문에 int 처리
    divisor = []
    for i in range(1, m+1):
        if n % i == 0:
            divisor.append(i)
            if i != n // i: # 25의 약수 5*5일때 5같은 약수 중복방지
                divisor.append(n // i)
            divisor.sort()
    except_me = divisor[:-1]
    # 언팩킹 활용
    if n == sum(except_me):
        print("{0} = ".format(n),end='')
        print(*except_me, sep=" + ")
        
    else:
        print("{0} is NOT perfect.".format(n))
        
    # ------------------------------------------------------------
    # 방법 2
    # 조인(리스트안 요소가 int기 때문에 리스트 상 문자열 변환 후 조인) , 리스트 컴프리헨션 사용, f파싱 사용
    while True:
        n = int(input())
        if n == -1:
            break
        divs = [i for i in range(1, n // 2 + 1) if n % i == 0]
        if sum(divs) == n:
            print(f"{n} = {' + '.join(str(i) for i in divs)}")
        else:
            print(f'{n} is NOT perfect.')