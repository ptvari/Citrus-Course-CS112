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
root1.geometry("300x300")
#title of gui
root1.title("The Offical Secret Nock Picker!")
title_label= tk.Label(root1, text='The Offical Secret Nock Picker!', bg='light blue')
title_label.pack(pady=20)


#first frame for border for entry frame
borderframe= tk.Frame(root1,padx=50, pady=50, bg="blue")
borderframe.pack(pady=50)
title=tk.Label(borderframe, text='Please enter objects to pull from random picker!', pady=20, padx=20)
title.pack()
#second frame for entry and button
#entryFrame= tk.Frame(root1,width=200,height=200,bg='red')
#entryFrame.pack()
entry = tk.Entry(borderframe, width=25, font=("Times New Roman", 12))
entry.pack()


'''
def on_button_click():
    print("Button clicked! A function was executed.") # This prints to the console
button = tk.Button(
    inputFrame,
    text="Add",
    command=on_button_click
)
button.grid()
'''
secretknock = choice_buddy_picker(random_items=['tat_ta','ding'],best_outta=11)
formatOutString = 'The secret knock was {} ' .format(secretknock)

#makes your window loop
root1.mainloop()
