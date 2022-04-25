# 2022_04_25_1
# 터렛
# 두 원을 지나는 방정식 이용

for _ in range(int(input())):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    d = ((x1-x2)**2 + (y1-y2)**2)**0.5
    if d == 0 and r1 == r2: # 위치의 개수가 무한대 == 거리가 같고 동심원인 경우
        print(-1)
    elif abs(r1-r2) < d < abs(r1+r2): # 두 점에서 만나는 경우
        print(2)
    elif r1 + r2 == d or abs(r1-r2) == d: # 한 점에서 만나는 경우(접히는 경우 == 외접 or 내접)
        print(1)
    
    else: # 만나지 않는 경우 (외부에서 만나지 X, 내부에 포함, 동심원인 경우)
        print(0)

        

for _ in range(int(input())):
    x1, y1, r1, x2, y2, r2 = list(map(int, input().split()))
    
    # 두 원의 중심 사이의 거리
    d = ((x1 - x2)**2 + (y1 - y2)**2) ** 0.5
    
    if d == 0:    # 두 원의 중심이 같을 경우
        if r1 == r2: # 두 원의 크기가 같아 겹치는 경우
            print(-1)
        else:                     # 한 원이 다른 원 안에 들어가 있는 경우(동심원)
            print(0)
    else:            # 두 원의 중심이 다를 경우
        if r1 + r2 == d or abs(r2-r1) == d: # 외접 or 내접
            print(1)
        elif ((abs(r1-r2) < d) and (d < r1+r2)): # 두 점에서 만날 때
            print(2)
        else: # 완전히 떨어지거나 내부 포함(not 동심원)
            print(0)