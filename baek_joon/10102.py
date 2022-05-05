# 2022_05_05_1
# 개표
vote_num = int(input())
word = input()
a_num = word.count('A')
b_num = word.count('B')
if a_num > b_num:
    print("A")
elif a_num < b_num:
    print("B")
else:
    print("Tie")