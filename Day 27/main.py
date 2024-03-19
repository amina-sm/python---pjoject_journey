from tkinter import *


def button_clicked():
    print(" I got Clicked")
    new_text = input.get()
    my_label.config(text=new_text)


window = Tk()
window.title("My first GUI program")
window.minsize(width=500,  height=300)
window.config(padx=100, pady=200)

# LABEL

my_label = Label(text="I am a Label", font=("Arial", 24, "bold"))


my_label["text"] = "New text"
my_label.config(text="New Text")
my_label.grid(column=1, row=0)
my_label.config(padx=50, pady=50)

# BUTTON
button = Button(text="Click Me", command=button_clicked)
button.grid(column=2, row=1)

new_button = Button(text="New button", command=button_clicked)
new_button.grid(column=3, row=0)
# Entry
input = Entry(width=10)
print(input.get())
input.grid(column=4, row=2)


window.mainloop()
