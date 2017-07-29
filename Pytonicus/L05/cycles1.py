# i = 0
# while i < 10:
# 	# i = i + 1
# 	print(i)

# n = ""
# while name != "Рукижат":
# 	name = input("Введите имя")
# 	print("Вы не подходите")
# print("Всё верно")

while  True:
	name = input("Введите имя: ")
	if name == "Рукижат":
		print("Все верно")
		break
	if name == "Саид":
		print("Выне подходите")
		continue
	print("Вы не подходите")
