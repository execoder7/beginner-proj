from tkinter import *
from tkinter.font import Font


root = Tk()
root.title('ToDo App')
root.geometry("600x500")


# Defining font
my_font = Font(family="Agency FB", size =30, weight='bold')
my_font_20 = Font(family="Agency FB", size =20, weight='bold')

my_frame = Frame(root)
my_frame.pack(pady=10)

lbl = Label(my_frame, text="Add an Item", font=my_font_20)
lbl.pack()


# Create listbox
my_list = Listbox(my_frame, font=my_font, width=25, height=5, bg='SystemButtonFace',bd=0,fg='#464646',highlightthickness=0,selectbackground='#a6a6a6',activestyle='none')
my_list.pack(side=LEFT,fill=BOTH)

items = []
for item in items:
    my_list.insert(END, item)

# Create scrollbar
my_scrollbar = Scrollbar(my_frame)
my_scrollbar.pack(side=RIGHT, fill=BOTH)

# Add scrollbar
my_list.config(yscrollcommand=my_scrollbar.set)
my_scrollbar.config(command=my_list.yview)

# Create entry box to add items to the list
my_entry = Entry(root, font=('Helvetica', 15))
my_entry.pack(pady=15)

# Create a btn frame
btn_frame = Frame(root)
btn_frame.pack(pady=20)


# FUNCTIONS
def del_item():
    my_list.delete(ANCHOR)

def add_item():
    
    if my_entry.get() and my_entry.get().strip():
        my_list.insert(END, my_entry.get())
        my_entry.delete(0, END)



# Add some buttons
add_btn = Button(btn_frame, text="Add Item", command=add_item)
del_btn = Button(btn_frame, text="Delete Item", command=del_item)

add_btn.grid(row=0,column=0)
del_btn.grid(row=0,column=1, padx=13)


root.mainloop()

