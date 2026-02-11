"""
This implementation will be done on a tkinter gui
to show output in a more fun way
Also will use input widgets in class
feb 10 2026
"""
import tkinter as tk
from SecretKnockPick import choice_buddy_picker
#tk gui requires a root

root1=tk.Tk()
#place a frame for the input widgets
root1.title("The Offical Secret Nock Picker!")
inputFrame= tk.Frame(root1,width=200,height=100,bg='light blue')
title_label= tk.Label(root1, text='The Offical Secret Nock Picker!')
title_label.pack(pady=10)

inputFrame.pack()
secretknock = choice_buddy_picker(random_items=['tat_ta','ding'],best_outta=11)
formatOutString = 'The secret knock was {} ' .format(secretknock)

#makes your window loop
label = tk.Label(inputFrame, text=formatOutString, bg='red')
label.grid(row=0,column=0,padx=10,pady=10)
root1.mainloop() 
