# 2022_05_02_1
# 사분면
axis = 0
q1 = 0
q2 = 0
q3 = 0
q4 = 0

for _ in range(int(input())):
    x, y = map(int, input().split())
    if x == 0 or y == 0:
        axis += 1
    elif x > 0 and y > 0:
        q1 += 1
    elif x < 0 and y > 0:
        q2 += 1
    elif x < 0 and y < 0:
        q3 += 1
    else:
        q4 += 1
print("Q1: {0}\nQ2: {1}\nQ3: {2}\nQ4: {3}\nAXIS: {4}".format(q1, q2, q3, q4, axis)) 