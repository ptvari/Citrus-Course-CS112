"""""
This is so that we can pick the secret knock for our class
1/30/26
Pick at random from a list that we propose
"""
import random
#This is going to be a list, in other languages they call it arrays
#This is a static list so far buddy hard coded.
choices = ['tat ta rata +4','one knock 2 coughs','ding ding sneeze']
#These list will be dynamic
tat_ta = []
one_knock = []
ding = []
print(choices)
#sample output
for i in range(5):
    print('the pick choice is')
    pick =random.choice(choices)
    tat_ta.append(pick)
print("What got picked is:" "!!!!!!")
print(tat_ta)
print(one_knock)
print(ding)
#This does not yet have input
