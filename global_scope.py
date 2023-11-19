import random
EASY_LEVEL_TURNS= 10
HARD_LEVEL_TURNS= 5

def check(guess, answer, turns):
    if guess > answer:
        print("Too high")
        return turns-1
    elif guess < answer:
        print("Too low")
        return turns -1
    else:
        print(f"You got it! The answer was {answer}.")  
        
def set_difficult():
    level=input("Choose difficult. Type 'easy' or 'hard': ")
    if level== "easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS    
    
def game():    
    print("Welcome to number guessing game!")
    print("I'm thinking of a number between 1 and 100")
    
    numbers = list(range(1, 101))  # Generate a list of numbers from 1 to 100
    answer=random.choice(numbers)
    print(f" Pssst, the correct answer is {answer}")
    turns=set_difficult()
   
    guess=0
    while guess != answer:
        print(F" You have {turns} attempts remaining to guess the number.")
        guess=int(input(" Make a guess: "))
        turns=check(guess, answer, turns) 
        if turns==0:
            print("you loose") 
            return     
                    
game()            
                
    