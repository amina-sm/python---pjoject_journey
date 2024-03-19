from tkinter import *
import pandas as pd
import random
import os

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
to_learn = {}

# Create 'data' directory if it doesn't exist
data_directory = "data"
if not os.path.exists(data_directory):
    os.makedirs(data_directory)

try:
    data = pd.read_csv(
        "E:\\ASM\\Journey1\\flash-card-project-start\\data\\french_words.csv")
except FileNotFoundError:
    original_data = pd.read_csv(
        "E:\\ASM\\Journey1\\flash-card-project-start\\data\\french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")


def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    Canvas.itemconfig(card_title, text="French", fill="black")
    Canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    Canvas.itemconfig(card_background, image=card_front_img)
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    Canvas.itemconfig(card_title, text="English", fill="white")
    Canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    Canvas.itemconfig(card_background, image=card_back_img)


def is_known():
    if current_card in to_learn:
        to_learn.remove(current_card)
        data = pd.DataFrame(to_learn)
        data.to_csv("data/words_to_learn.csv", index=False)
    next_card()


window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

Canvas = Canvas(width=800, height=526)
card_front_img = PhotoImage(
    file="E:/ASM/Journey1/flash-card-project-start/images/card_front.png")
card_back_img = PhotoImage(
    file="E:/ASM/Journey1/flash-card-project-start/images/card_back.png")
card_background = Canvas.create_image(400, 263, image=card_front_img)
card_title = Canvas.create_text(
    400, 150, text="Title", font=("Ariel", 40, "italic"))
card_word = Canvas.create_text(
    400, 263, text="word", font=("Ariel", 60, "italic"))
Canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
Canvas.grid(row=0, column=0, columnspan=2)

cross_image = PhotoImage(
    file="E:/ASM/Journey1/flash-card-project-start/images/wrong.png")
unknown_button = Button(
    image=cross_image, highlightthickness=0, command=next_card)
unknown_button.grid(row=1, column=0)

check_image = PhotoImage(
    file="E:/ASM/Journey1/flash-card-project-start/images/right.png")
known_button = Button(
    image=check_image, highlightthickness=0, command=is_known)
known_button.grid(row=1, column=1)

next_card()
window.mainloop()
