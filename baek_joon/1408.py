# 2022-02-13_2

now_h, now_m, now_s = input().split(":")
now_total = int(now_h)*3600 + int(now_m)*60 + int(now_s)
start_h, start_m, start_s = input().split(":")
start_total = int(start_h)*3600 + int(start_m)*60 + int(start_s)

if now_total > start_total:
    time_remaining = 24*3600 + start_total - now_total
else:
    time_remaining = start_total - now_total

tr_h = time_remaining // 3600

# 숫자가 일의 자리 수일 경우 '0'을 추가 => print("%02d:%02d:%02d") 첫째수: 빈칸 채울 숫자, 둘째 수: 몇 째 자리까지 채울건인가로 포맷팅 대체 가능
if tr_h // 10 == 0 or tr_h == 0:
    tr_h = '0' + str(tr_h) 

tr_m = (time_remaining % 3600) // 60
if tr_m // 10 == 0 or tr_m == 0:
    tr_m = '0' + str(tr_m) 

tr_s = (time_remaining % 3600) % 60
if tr_s // 10 == 0 or tr_s == 0:
    tr_s = '0' + str(tr_s) 

print(str(tr_h) + ":" + str(tr_m) + ":" + str(tr_s))
