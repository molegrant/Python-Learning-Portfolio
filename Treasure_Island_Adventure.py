print(r'''
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
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
#Choice 1
choice1 = input('You find yourself at a crossroads, where do you want to go? ' 
                'Type "left", "right" or "straight" ').lower()
if not choice1 == "left":
    print("You fall into a hole. Game Over")
else:
    #Choice 2
    choice2 = input('You\'ve come to a lake. You can see an island in the middle of it. '
                    'Type "wait" to wait for a boat. '
                    'Type "swim" to swim across. ').lower()
    if not choice2 == "swim":
        print("You drown. Game Over")
    else:
        #Choice 3
        choice3 = input('You find yourself at three coloured doors: Red, Yellow and Blue. '
                    'Which door do you want to go through? ').lower()
        if choice3 == "Red":
            print("You are burned alive. Game Over.")
        elif choice3 == "Blue":
            print("You are eaten by beasts. Game Over.")
        else:
            print("You win! Congratulations.")