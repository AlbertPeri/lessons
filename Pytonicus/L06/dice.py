from random import randint   

player1 = {"сумма": 1000}
player2 = {"сумма": 1000}
player1["имя"] = input("Введите имя игрока: ")
player2["имя"] = input("Введите имя игрока: ")


while True:
	player1["ставка"] = int(input(player1["имя"] + " введите ставку: "))
	if player1["ставка"] > player1["сумма"]:
		player1["ставка"] = player1["сумма"]

	if player1["ставка"] <= 0:
		int(input(player1["имя"] + " ноль ввести нельзя: "))
		if player1["ставка"] <= 0:
			print("Презапустите игру вы не ввели правельно")
			break

	player2["ставка"] = int(input(player2["имя"] + " введите ставку: "))
	if player2["ставка"] > player2["сумма"]:
		player2["ставка"] = player2["сумма"]


	if player2["ставка"] <= 0:
		int(input(player2["имя"] + " ноль ввести нельзя: "))
		if player1["ставка"] <= 0:
			print("Презапустите игру вы не ввели правельно")
			break

	if player2["ставка"] < player1["ставка"]:
		player2["ставка"] = int(input(player2["имя"] + " введите ставку как у первого игрока или больше: "))
		print("Презапустите игру вы не ввели правельно")
		break


	player1["бросок"] = randint(1,12)
	player2["бросок"] = randint(1,12)
	print(player1["имя"], "выбросил",player1["бросок"])
	print(player2["имя"], "выбросил",player2["бросок"])

	if player1["бросок"] > player2["бросок"]:
		print(player1["имя"], "выйграл ставку")
		player1["сумма"] += player2["ставка"]
		player2["сумма"] -= player1["ставка"]


	if player2["бросок"] > player1["бросок"]:
		print(player1["имя"], "выйграл ставку")
		player2["сумма"] += player1["ставка"]
		player1["сумма"] -= player2["ставка"]
	else:
		print("ничья")
	print(player1["имя"], player1["сумма"])
	print(player2["имя"], player2["сумма"])

	if player1["сумма"] <= 0:
		print(player2["имя"] ,"победил")
		break

	if player2["сумма"] <= 0:
		print(player1["имя"] ,"победил")
		break







