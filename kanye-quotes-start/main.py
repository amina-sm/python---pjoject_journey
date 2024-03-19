from tkinter import *
import requests

response = requests.get(url="https://api.kanye.rest")
response.raise_for_status()

data = response.json()["quote"]


def get_quote():
    response = requests.get(url="https://api.kanye.rest")
    response.raise_for_status()
    data = response.json()["quote"]

    # Update the text of the canvas item with the fetched Kanye quote
    canvas.itemconfig(quote_text, text=data)


window = Tk()
window.title("Kanye Says...")
window.config(padx=50, pady=50)

canvas = Canvas(width=300, height=414)
background_img = PhotoImage(file="./kanye-quotes-start/background.png")
canvas.create_image(150, 207, image=background_img)
quote_text = canvas.create_text(150, 207, text=data, width=250, font=(
    "Arial", 10), fill="white")
canvas.grid(row=0, column=0)

kanye_img = PhotoImage(file="./kanye-quotes-start/kanye.png")
kanye_button = Button(image=kanye_img, highlightthickness=0, command=get_quote)
kanye_button.grid(row=1, column=0)

window.mainloop()
