# 2022_02_15_2
receipt_list = []

for _ in range(10):
    receipt_list.append(int(input()))
print(receipt_list[0] - sum(receipt_list[1:]))