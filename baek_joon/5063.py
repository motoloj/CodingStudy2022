# 2022_05_06_1
# TGN
for _ in range(int(input())):
    r, e, c = map(int, input().split())
    ad_profit = e - c
    if r < (ad_profit):
        print('advertise')
    elif r == (ad_profit):
        print('does not matter')
    else:
        print('do not advertise')