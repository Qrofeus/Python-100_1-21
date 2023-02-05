# Treasure Island - Choose your own adventure
print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/______/_
*******************************************************************************
''')
print("Welcome to Treasure Island\nYour mission is to find the treasure")

choice_1 = input("You are at a crossroad, will you go left or right?\n>>").lower()
if choice_1 != "left":
    print("You fell into a hole\nGAME OVER")
    exit()

choice_2 = input("You come across a river, will you swim or wait?\n>>").lower()
if choice_2 != "wait":
    print("You were attacked by trout\nGAME OVER")
    exit()

choice_3 = input("You come across 3 doors, which door will you open?\nRed, Blue or Yellow\n>>").lower()
if choice_3 == "red":
    print("You were burned by fire\nGAME OVER")
elif choice_3 == "blue":
    print("You were eaten by beasts\nGAME OVER")
elif choice_3 == "yellow":
    print("You found the treasure...\nYOU WIN")
else:
    print("GAME OVER")
