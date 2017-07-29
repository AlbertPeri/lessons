import json

with open("piplse.json", "r", encoding="utf-8") as f:
	data = f.read()

data = json.loads(data)
print(data["Магомед"] ["возраст"])
data["Магомед"] ["любимое блюдо"].append("Пицца")
print(data)

data2 = json.dumps(data)

with open("piplse.json", "w", encoding="utf-8") as f:
	f.write(data2)

for name in data:
	print(name, data[name]["возраст"])