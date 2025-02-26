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
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_ 
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_ 
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____ 
/______/______/______/______/______/______/______/______/______/______/
*******************************************************************************
''')

print("\nWelcome to Treasure Island.\n")
print("Your mission is to find the treasure.\n")

choice1 = input("You are at a crossroad. Where do you want to go? Type 'Left' or 'Right':\n").lower()

if choice1 == "left":
    print("\nYou've come to a lake. There is an island in the middle of the lake.\n")
    
    choice2 = input("Type 'wait' to wait for a boat. Type 'swim' to swim across:\n").lower()
    
    if choice2 == "wait":
        print("\nYou arrive at the island unharmed.\n")
        print("There is a house with 3 doors: One red, one yellow, and one blue.\n")
        
        choice3 = input("Which color do you choose? Type 'Red', 'Yellow', or 'Blue':\n").lower()
        
        if choice3 == "red":
            print("\nIt's a room full of fire. Game Over.\n")
        elif choice3 == "yellow":
            print("\nYou found the treasure. Congratulations! You Win!\n")
        elif choice3 == "blue":
            print("\nYou enter a room of beasts. Game Over.\n")
        else:
            print("\nGame Over.\n")
    else:
        print("\nYou got attacked by an angry trout. Game Over.\n")
else:
    print("\nYou fell into a hole. Game Over.\n")
