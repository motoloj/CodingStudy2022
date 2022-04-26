# 2022_04_26_1
# 다리 놓기
for _ in range(int(input())):
    n, m = map(int, input().split())
    all_m = 1
    all_n = 1
    if n > m:
        for i in range(m, 0, -1):
            all_m *= i 
        for g in range(n, n-m, -1):
            all_n *= g
        print(all_n//all_m)
        
    elif n < m:
        for i in range(n, 0, -1):
            all_n *= i 
        for g in range(m, m-n, -1):
            all_m *= g
        print(all_m//all_n)
        
    else:
        print(1)