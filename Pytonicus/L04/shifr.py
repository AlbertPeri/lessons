text = input("Введи слово который хочешь зашифровать: ")
text = text[len(text) // 3:] + text[:len(text)//3]
print(text)

text2 = input("Нажми 1 если хочешь рашифровать нажми 2 нет: ")
if text2 == "1":
	text = text[len(text) // -6:] + text[:len(text)//-6]
	print(text)
elif text2 == "2":
	print("Ну ладно")

