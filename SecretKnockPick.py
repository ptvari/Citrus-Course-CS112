"""""
This is so that we can pick the secret knock for our class
1/30/26
Pick at random from a list that we propose
"""
import random
#This is going to be a list, in other languages they call it arrays
#This is a static list so far buddy hard coded.
#This is my function
def choice_buddy_picker(random_items,best_outta):
    choices = random_items
    tat_ta, oneknock, ding = [],[],[]
    #the_input_buddy=int(input("How many times do you wanna run the loop, BUDDY?: "))
    for i in range(best_outta):
        pick=random.choice(choices)
        if pick == choices[0]:
            tat_ta.append(pick)
        elif pick == choices[1]:
            oneknock.append(pick)
        else:
            ding.append(pick)
    a=len(tat_ta)
    b=len(oneknock)
    c=len(ding)
    print(a,b,c)
    winner = max(a,b,c)
    if winner == a:
        return winner, choices[0]
    elif winner == b:
        return winner, choices[1]
    else:
     return winner, choices[2]
choice_value= ''
choices = []
while choice_value != 'x':
    choice_value = input('Enter choices as phases enter x when done ')
    if choice_value == 'x':
        break
    choices.append(choice_value)
    print('These are the choices buddy!!!!!!: ', choices)

winning_number,option = choice_buddy_picker(choices,10000)
print(winning_number,option)




