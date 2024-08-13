import random
words=["water", "banana", "pineapple", "watermelon", "pants", "plant", "blanket", "hoodie", "glasses", "keyboard", "bottle", "notebook"]
word=random.choice(words)
#print(word)
print("Welcome to Guess The Word!!! You have 12 guesses to correctly guess the word")
turns=12
guesses=''
print("Guess the Character")
while turns>0:
    failed=0
    for x in word:
        if x in guesses:
            print(x, end=" ,")
        else:
            print("_")
            failed+=1

    if failed==0:
        print("You Win!!!")
        print("The word is", word)
        break
    guess=input("Guess a Character: ")
    guesses+=guess
    if guess not in word:
        turns-=1
        print("Incorrect, Try again")
        print("You have", turns, "left")
        if turns==0:
            print("You ran out of turns, You lose")
#Design the tkinter for this