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
tat_ta,oneknock,ding= [],[],[]
print('These are the choices buddy!!!!!!:',choices)
the_input_buddy=int(input("How many times do you wanna run the loop, BUDDY?:"))
for i in range(the_input_buddy):
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
    print(choices[0])
elif winner == b:
    print(choices[1])
else:
    print(choices[2])



"""""
for x in tat_ta:
    print(c,x)
    c = c +1
for y in oneknock:
    print(d,y)
    d = d +1
for z in ding:
    print(e,z)
    e=e+1
"""""


"""
if tat_ta == len()
    print('This one wins buddy!')
elif:
#This does not yet have input
"""
