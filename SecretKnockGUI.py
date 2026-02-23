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
root1.geometry("450x350")
#title of gui
root1.title("The Offical Secret Nock Picker!")
title_label= tk.Label(root1, text='The Offical Secret Nock Picker!', bg='light pink')
title_label.pack(pady=10, padx=10)


#first frame for border for entry frame
borderframe= tk.Frame(root1,padx=40, pady=40, bg="blue")
borderframe.pack(pady=40)
#This changes based on what wins and shows how many times it got picked.
label_text=tk.StringVar()
label_text.set("Please enter objects to pull from random picker!")
title=tk.Label(borderframe, textvariable=label_text, pady=5, padx=5, width=35)
title.pack()

entry = tk.Entry(borderframe, width=30, font=("Times New Roman", 12))
entry.pack(pady=10)
#This will be th global list adder
items_list=[]
def list_adder():
    user_input= entry.get()
    if user_input != "":
        items_list.append(user_input)  # add to list
        print("Option was added")
        print(f"Added: {user_input}")  # show what was added
        print("Full list:", items_list)  # show full list in terminal
        label_text.set("Items: " + ", ".join(items_list))
        entry.delete(0, tk.END)  # clear the box after adding

#This button allows the user to append to the global list
buttonadd = tk.Button(
    borderframe,
    text="Add",
    command=list_adder
)
#This runs the picker by using the global list from before
def run_da_picker():
    if items_list:
        secretknock = choice_buddy_picker(random_items=items_list, best_outta=100)
        print("Machine is alive!!!")
        formatOutString = 'The secret knock was {} '.format(secretknock)
        print(formatOutString)
        label_text.set(formatOutString)

#This button is the start button for the whole random picker, when it presses start, it uses the "run_da_picker" to show what won and how many times.
buttonstart=tk.Button(
    borderframe,
    text="Start!",
    command=run_da_picker
)
buttonadd.pack(side="left", padx=5)
buttonstart.pack(side="right", padx=5)

#makes your window loop
root1.mainloop()
