# rock paper scissor game
import random
user_choice=int(input('What do you choose? type "0" for rock, type "1" for paper and type "2" for scissor\n'))
computer_choice=random.randint(0,2)
print(f"computer choice is {computer_choice}")
if user_choice>=3:
    print("You have enter an invalid choice")
elif user_choice==0 and computer_choice==2:
    print("You win")    
elif computer_choice > user_choice:
    print("you loose")  
elif computer_choice== user_choice:
    print("it is a draw")   
elif computer_choice==0 and user_choice==2:
    print ("You win")
elif user_choice > computer_choice:
    print("you win")
           