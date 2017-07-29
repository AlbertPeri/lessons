class DayError(Exception):
    pass
    
class MonthError(Exception):
    pass

while True:
    try:
        date = input("Введите дату рождения дд.мм.гггг: ")
        day = int(date[:2])
        month = int(date[3:5])
        year = int(date[6:])
        print(day, month, year)
        if day < 1 or day > 31:
            raise DayError
        if month < 1 or month > 12:
            raise MonthError

        if (day > 22 and month == 3) or (day < 20 and month == 4):
            print("Ты - Овень :)")
        
        if (day > 21 and month == 4) or (day < 21 and month == 5):
            print("Ты - телец <3")

        if (day > 22 and month == 5) or (day < 21 and month == 6):
            print("Ты - близнец '_' ")

        if (day > 22 and month == 6) or (day < 23 and month == 7):
            print("Ты - рак :0")

        if (day > 22 and month == 7) or (day < 23 and month == 8):
            print("Ты - лев ;)")

        if (day > 22 and month == 8) or (day < 23 and month == 9):
            print("Ты - дева )))")

        if (day > 22 and month == 9) or (day < 23 and month == 10):
            print("Ты весы")

        if (day > 22 and month == 10) or (day < 22 and month == 11):
            print("Ты - скорпион")

        if (day > 21 and month == 11) or (day < 22 and month == 12):
            print("Ты - стрелей")

        if (day > 21 and month == 12) or (day < 20 and month == 1):
            print("Ты - козерог")

        if (day > 19 and month == 1) or (day < 19 and month == 2):
            print("Ты - водолей")

        if (day > 18 and month == 2) or (day < 21 and month == 3):
            print("Ты - рыба :()")

        if (day > 28 and day < 32 and month == 2):
            print ("В феврале нету столько дней")


    except ValueError:
        print("Введите правельном формате")
    except DayError:
        print("Введите правельный день")
    except MonthError:
        print("Введите правельный месяц")
