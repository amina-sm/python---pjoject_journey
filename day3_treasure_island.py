#  A project of treasure island game
print("Welcome ton  Tressure island.")
print("Your mission is to find  the Treasure")

choice1=input('Your are at a cross road. where do you want to go? Type "left" or "right" \n ').lower()
if choice1== "left":
    choice2= input('You came to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across.\n').lower()
    if choice2=="wait":
        choice3= input('You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which color do you choose? "red", "blue" or "yellow" \n').lower()
        if choice3=="red":
            print("Burned on fire.\n Game over")
        elif choice3=="blue":
            print("Eaten by beasts.\n Game Over.")
        elif choice3=="yellow":
            print("You win")
        else:
            print("Game over.")         
    else:
        print("Attacked by trout.\n Game over.")  
else:
    print("Fall into a hole.\n Game over")               