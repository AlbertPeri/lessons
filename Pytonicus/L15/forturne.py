import random

with open("принц.txt", "r", encoding="utf-8") as f:
	text = f.read()
while True:
	vubor = input("Что ты хочешь узнать?\n1.дату своей смерти\n2.предсказание на будующие: ")
	if vubor == "1":
		death = input("Ты точно хочешь узнать дату своей смерти \n1.да\n2.нет: ")

		number = random.randint(1, 31)
		number2 = random.randint(1, 12)
		number3 = random.randint(2017, 2095)
		if death == "1" or death == "да":
			print("Мне очень жаль но это правда:", number,".",number2,".",number3)
		elif death == "2" or death == "нет":
			print("Ну окей")
 
	elif vubor == "2":
		stop = input("Введите вопрос: ")
		if stop == "стоп":
			print("Ты черт и кидала не веришь в мои способности")
			break
		answer_len = 26
		position = random.randint(0, len(text) - answer_len)
		answer = text[position:position + answer_len + 1]
		answer = answer[answer.find(" ") + 1: answer.rfind(" ")]
		print(answer)

	else:
		print("Я не понимаю тебя")



