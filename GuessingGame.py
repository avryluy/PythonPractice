import  random
secretnumber = random.randint(1, 20)

#Ask the User for a guess
for guessesTaken in range(1,7):
    print('Take a guess.')
    guess = int(input())

    if guess < secretnumber:
        print('Too low. Try again')
    elif guess >  secretnumber:
        print('Too high. Try again.')
    else:
        break #This condition is a correct guess and breaks the loop

#Outputs response for Win or if the User exceeds guess limit    
if guess == secretnumber:
    print('Nice! You got it right in ' + str(guessesTaken) + ' guesses!')
else:
    print('You are taking too long. The correct guess was ' + str(secretnumber))