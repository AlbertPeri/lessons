class House:
    def __init__(self, fundament, karkas, krusha):
        self.fundament = fundament
        self.karkas = karkas
        self.krusha = krusha

dom = House("Фундамент:\nВ:10м\nД:100м\nШ:15м", "\nКаркас:\nВ:35м", "\nКрыша:\nЦ:синий\nВ:5м")
print(dom.fundament, dom.karkas, dom.krusha)

