import random
word_list=["ardvark", "baboon", "camel"]
#Random choose a letter from a list
choosen_word=random.choice(word_list)
print(f'your choosen word is {choosen_word}')
#ask user to inter any letter
display= []
for _ in range(len (choosen_word)):
    display += "_"
print(display)

end_of_game= False
while not end_of_game:
    guess=input("Guess any letter found in the list: ").lower()
#matching letter and a choosen_word
    for position in range(len(choosen_word)):
        letter=choosen_word[position]
        #print(f"current position: {position}\n current letter: {letter}\n Guessed letter: {guess}")
        if letter==guess:
         display[position]=letter

    print(display)

    if "_" not in display:
        end_of_game= True
        print("You win")