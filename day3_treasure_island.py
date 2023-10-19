#  A project of treasure island game
print("Welcome ton  Tressure island.")
print("Your mission is to find  the Treasure")

cross_road=input('Your are at a cross road. where do you want to go? Type "left" or "right" ')
if cross_road== "left":
    lake= input('You came to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across.')
    if lake=="wait":
        door= input('You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which color do you choose? "red", "blue" or "yellow" ')
        if door=="red":
            print("Burned on fire.\n Game over")
        elif door=="blue":
            print("Eaten by beasts.\n Game Over.")
        elif door=="yellow":
            print("You win")
        else:
            print("Game over.")         
    else:
        print("Attacked by trout.\n Game over.")  
else:
    print("Fall into a hole.\n Game over")               