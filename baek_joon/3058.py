# 2022_04_03_1
# 짝수를 찾아라

for _ in range(int(input())):
   even =  [i for i in map(int, input().split()) if i % 2 == 0 ]
   print(sum(even), min(even))