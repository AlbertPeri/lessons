import random

with open("дата.txt", "r", encoding="utf-8") as f:
	text = f.read()
while True:
	death = input("Ты хочешь узнать дату своей смерти \n1.да\n2.нет\n3.узнать с помошью теста: ")

	answer_len = 10
	position = random.randint(0, len(text) - answer_len)
	answer = text[position:position + answer_len + 1]

	number1 = random.randint(2036, 2095)
	number2 = random.randint(2030, 2070)
	number3 = random.randint(2020, 2057)

	if death == "1" or death == "да":
		print("Мне очень жаль но это правда:", answer)

	elif death == "2" or death == "нет":
		print("Ну окей")
		break

	elif death == "3":
		vopros1 = input("Вы курите?: ")
		vopros2 = input("Занемаетесь ли вы спортом?: ")
		vopros3 = int(input("Как вы часто болеете? В год...: "))
		if vopros1 == "да" and vopros2 == "да":
			print("Вы умрёте:", number2)
		elif vopros1 == "нет" and vopros2 == "нет":
			print("Вы умрёте:", number2)
		elif vopros1 == "да" and vopros2 == "нет":
			print("Вы умрёте:", number3)
		elif vopros1 == "нет" and vopros2 == "да":
	elif death == "stop":
		print("Ну окей")
		break
		