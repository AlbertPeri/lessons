class Plant:
	def __init__(self, name, age, grade):
		self.name = name
		self.age = age
		self.grade = grade

	def grow(self, years):
		self.age += years

	def show_age(self):
		print(self.name, ":", self.age)


class Tree(Plant):
	def grow(self, years):
		super().grow(years)
		print("ФФФФФФФФФааааааааааааааааааа")

class EvilTree(Tree):
	def kill(self, target):
		print(self.name, "убило и съело", target.name)
	

class Flower(Plant):
	def __init__(self, name, age, grade):
		super().__init__(name, age, grade)
		self.is_bloom = True

	def bloom(self):
		self.bloom = True
		print(self.name,"расцвел")

class MutantPlant:
	def __init__(self, plants):
		self.plants = plants

	def show_plants(self):
		print("Я состаю из:")
		for plant in self.plants:
			print(plant.name)

	def eat_my_part(self, part):
		if part in self.plants:
			self.plants.remove(part)
			part.grow(1)
		else:
			print("Нечино есть")
class Dubinus:
	def __init__(self):
		self.name = "Дубинус"

	def grow(self, age):
		print("Я дубинус")

spruse = Tree("Чакар", 102, "Ель")
spruse.grow(5)
spruse.show_age()

maga = Flower("Магомед", 1, "Роза")
maga.grow(3)
maga.show_age()
maga.bloom()
print(maga.is_bloom)

fatima = EvilTree("Фатима", 14, "Береза")
fatima.kill(maga)

dubunus = Dubinus()
arsen = MutantPlant([fatima, spruse, maga, dubunus])
arsen.show_plants()
arsen.eat_my_part(spruse)
arsen.show_plants()
