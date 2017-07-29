# dishes = ('суп','пелемени')
# soup, dumgligs = dishes
# print(soup)
# x, y = "морковь" , "латук"
# print(y)

games = {"ведьмак","крейзер", "весёлая ферма", "ведьмак", "ведьмак",}
print(games)
artur_games = {"cod","csgo","весёлая ферма"}
print(games|artur_games) #Объяденение
print(games&artur_games) #пересечение
print(games-artur_games) #разность

games = set() # Пустое множество


games_dict = {
	"Ведьмак":"Ведьмак и монстры",
    "Дизонред":"О телехранителе и крысах",
    "Фолуат3":"Сын пытается найти отца"
 }
print(games_dict["Дизонред"])
games_dict["Skyrim"] = "Драконы и скума"
print(games_dict)
games_dict["Ведьмак"] = "мужик с белами волосами и  всякие кулачные бои"