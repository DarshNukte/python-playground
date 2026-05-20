ascii_art = r'''*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************'''


print("Welcome to Treasure Island.\nYour mission is to find the treasure.")
print("You are at a crossroad")
if input('Where would you like to go?\n"left" or "right"\n').lower() == "left":
    print('You are now at the Ganga river. Would you swim across or wait for a boat?\n"swim" or "wait"')
    if input().lower() == "wait":
        print("Now there are three doors in front of you.")
        print("Red, Blue and Yellow. Treasure is behind one of the door.")
        print('Which door would you enter? "Red", "Blue" or "Yellow"')
        doorImp = input().lower()
        if doorImp == "yellow":
            print("Congratulations!! You won the game.")
            print(ascii_art)
        elif doorImp == "red":
            print("You got burned by fire.\nGame Over")
        elif doorImp == "blue":
            print("You got eaten by beasts.\n Game Over.")
        else:
            print("Invalid Input.\nPlease Try Again.")
    else:
        print("You got attacked by a shark.\nGame Over.")
else:
    print("You fell into a hole.\nGame Over.")
