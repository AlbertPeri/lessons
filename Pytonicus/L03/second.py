import random

print("Учитаблицу умнажения")

while True:
	number = random.randint(0,10)
	number1 = random.randint(0,10)
	a = int(input(str(number) + "*" + str(number1)+ "="))
	if a == number * number1:
		print("Правельно")
	else:
		print("лох")