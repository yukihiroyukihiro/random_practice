import random

ans = random.randint(1, 10)
while True:
	x = int(input('請猜一個1~10的整數：'))
	if x == ans:
		print('猜對了！程式即將結束！')
		break

