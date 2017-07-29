import random

name1 = input("Введите имя первого игрока: ")
name2 = input("Введите иям второго игрока: ")

def get_card(player):
    while True:
        if not player["колода"]:
            break
        yield player["колода"].pop()
        


def turn(player1, player2):
    k = 0
    for card1, card2 in zip(get_card(player1),get_card(player2)):
        print(card1, card2)
        k += 2
        if card1[0] < card2[0]:
            player2["счет"] += k
            break

        elif card2[0] < card1[0]:
            player1["счет"] += k
            break  


suits = ["сердце","кирпич","пика","крест","валет","король","дама"]
deck = [(num,suit) for suit in suits for num in range(6,15)]
random.shuffle(deck)
# print(deck)
player1 = {}
player2 = {}
player1["колода"] = deck[:len(deck)//2]
player2["колода"] = deck[len(deck)//2:]
player1["счет"] = 0
player2["счет"] = 0
while True:
    turn(player1, player2)
    print("счет",name1,":",player1["счет"],"\n" "счет",name2,":", player2["счет"])
    input()
    if not player1["колода"]:
        print(name2 , "выйграл")
        break
    if not player2["колода"]:
        print(name1, "выйграл")
        break
    if not player1["колода"] and not player2["колода"]:
        print("ничья")