#Developer - Eden Iyamda
#This program prompt you to guess my name
print("Welcome!!")
guess_word = "Eden"
word = input("Enter my name")
guess_count = 1
guess_limit = 3
trial_off = False
while word != guess_word and not(trial_off) : 
    if guess_count < guess_limit:
        word = input("Try again")
        guess_count += 1
    else:
        trial_off = True
if trial_off:
    print("YOU LOSE!!")
else:
    print("You win!")


