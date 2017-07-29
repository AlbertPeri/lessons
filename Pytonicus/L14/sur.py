from random import randint, choice

class Character:
	def __init__(self, name, hp, damage):
		self.name = name
		self.hp = hp
		self.damage = damage

	def attack(self, other):
		damage = randint(0, self.damage)
		other.hp -= damage

	def show_hp(self):
		print(self.name, "жизни: ", self.hp) 

class SchoolScame(Character):
	def die(self):
		print(choice("Я умираюююю", "Это просто дичь", "Вызывае к Гамешу"))

class Hero(Character):
	def __init__(self, name, hp, damage):
		super().__init__(name, hp, damage)
		count = 0

class Game:
	def start(self):
		name = input("Введите имя героя: ")
		hero = Hero(name, 100, 15)
		school_scame = SchoolScame("Враг", 100, 5)
		while True:
			hero.attack(school_scame)
			school_scame.attack(hero)
			hero.show_hp()
			school_scame.show_hp()
			input()
			if school_scame.hp <= 0:
				school_scame.die()
				hero.count += 1
				school_scame = SchoolScame("гавнюк", 55, 5)
			if hero.hp <= 80:
				print("Второй уровень")
				school_scame = SchoolScame("Враг", 100, 10)
				hero.attack(school_scame)
				school_scame.attack(hero)
				hero.show_hp()
				school_scame.show_hp()
				input()
			if hero.hp <= 0:
				print(name + " умер. Игра окончена")
				break



game = Game()
game.start()




