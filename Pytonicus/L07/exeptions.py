# while True:
# 	try:
# 		number = int(input("Введите число: "))
# 		print(7 / number)
# 	except ValueError:
# 		print("Введите число!!!")
# 		break
# 	except ZeroDivisionError:
# 		print("На ноль делить нельзя")

# raise ZeroDivisionError

class ChakarError(Exception):
	pass
while True:
	try:
		name = input("Введите имя: ")
		if name.lower() == "чакар":
			raise ChakarError
		print(name, "молодец")
	except ChakarError:
		print("Фатальное ошибка нельзя вводить это слово")
		break