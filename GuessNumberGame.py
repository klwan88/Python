#This is a number guessing game between 1-10 and user only gets 5 tries.Made some hanges

def run(): #This function starts the game
    secretnum=random.randint(1, 10)
    for guesses in range (0, 6):
        print('You now guessed ' + str(guesses) + ' times. What is your guess now?')
        print('# is ' + str(secretnum))
        usernum=input()
        if int(usernum)==(secretnum):
            print('Congrats!You got it right! Would you like to play again? Y or N')
            playagain=input()
            if playagain=='Y':
                print('OK! Lets play again!')
                run() #Launches game again
            else:
                print('OK, we will stop now.')
                break
        elif guesses==4: #After failed 5 tries
            print('You have reached 5 tries already without getting it right. Would you like to play again?')
            playagain=input()
            if playagain=='Y':
                run()
            else:
                print('OK. We will stop now')
                break
        elif int(usernum)>secretnum:
            print('Your guess is too high!')
        elif int(usernum)<secretnum:
            print('Yourguess is too low!')


import random
print('Hi There! What is your name?')
name=input()
print("\n")
print('Hello ' + name + ', would you like to play a guessing game? Y or N')
play=input()
          
if play == 'Y':
    print("\n")
    print('I am thinking of a number between 1-10. You will have a total of 5 tries. Lets begin.')
    run()#Launches game
else:
    print('Have a good one!')
    
    
print('The End')
