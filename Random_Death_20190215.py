#This script picks a random person to die in a random way.

import random

def persontodie(candidate): #This def assigns candidate to name. For example, "persontodie(1)" pulls Philemon"
    if candidate==1:
        return 'Philemon'
    elif candidate==2:
        return 'Jean'
    elif candidate==3:
        return 'Hana'
    elif candidate==4:
        return 'Sharon'
    elif candidate==5:
        return 'Mike'
    elif candidate==6:
        return 'Kai'
    elif candidate==7:
        return 'Aaron'

def waystodie(way): #This def assigns ways to die. For example, "waystodie(1)" pulls "Die from Starvation."
    if way==1:
        return 'from starvation.'
    elif way==2:
        return 'from eating too many donuts.'
    elif way==3:
        return 'from working too hard.'
    elif way==4:
        return 'from drinking too much.'
    elif way ==5:
        return 'from boredom.'
    elif way ==6:
        return 'from racism.'

question=input('Lets play a game! We will pick one of you by random to kill off. Please type "y" to continue and "n" if you want to leave.')

print('Good! Lets roll the dice!')

while question=="y":
    print(persontodie(random.randint(1, 7)) + ' dies ' + waystodie(random.randint(1, 6)))
    print('Press "y" to play again or "n" to quit.')
    question=input()

print('Ok. Thanks for playing! Good bye!')
