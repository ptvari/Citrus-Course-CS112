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
root1.geometry("200x100")
#title of gui
root1.title("The Offical Secret Nock Picker!")
title_label= tk.Label(root1, text='The Offical Secret Nock Picker!', bg='light blue')
title_label.pack(pady=20)


#first frame for entry
entryFrame= tk.Frame(root1,width=400,height=400,bg='light blue')
entryFrame.pack()
entry = tk.Entry(entryFrame, width=25, font=("Times New Roman", 12))
entry.grid(row=0,column=2)


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
