f = open("filefile.txt", "w", encoding="utf-8")
f.write("коткоткоткоткоткоткоткокоткот\n")
f.write("ertertretert")
f.close()

# f = open("filefile.txt", "r", encoding="utf-8")
# text = f.read()
# f.close()
# print(text)

# f = open("filefile.txt", "r", encoding="utf-8")
# # text = f.readline()
# # text = f.readline()
# for line in f:
# 	print(line, end="")
# f.close()


with open("chakarTheBest.txt", "a", encoding="utf-8") as f:
	f.write("Песнь о сахоре")
