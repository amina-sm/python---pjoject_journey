from tkinter import *


def miles_to_km():
    miles = float(miles_input.get())
    km = miles * 1.609
    kilometer_result_label.config(text=f"{km}")


window = Tk()
window.title("Miles to Kilometer Converter")
window.config(padx=20, pady=20)


# Entry
miles_input = Entry(width=10)
miles_input.grid(column=1, row=0)


miles_label = Label(text="Miles", font=("Arial", 24, "bold"))
miles_label.grid(column=2, row=0)


is_equal_label = Label(text="is equal", font=("Arial", 24, "bold"))
is_equal_label.grid(column=0, row=1)


kilometer_result_label = Label(text="0", font=("Arial", 24, "bold"))
kilometer_result_label.grid(column=1, row=1)


kilometer_label = Label(text="Km", font=("Arial", 24, "bold"))
kilometer_label.grid(column=2, row=1)


calculate_button = Button(text="calculate", command=miles_to_km)
calculate_button.grid(column=1, row=2)


window.mainloop()
