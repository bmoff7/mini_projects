import tkinter

window = tkinter.Tk()
window.title("MILE TO KM CONVERTER")
window.minsize(width=250, height=110)


def button_clicked():
    new_text = miles_input.get()
    new_text = float  (new_text)*1.609
    number.config(text=new_text)


# Label
miles = tkinter.Label(text="Miles", font=("Arial", 14,), pady=15)
miles.grid(column=2, row=0)

# Label
km = tkinter.Label(text="Km", font=("Arial", 14,))
km.grid(column=2, row=1)

# Label
is_equal = tkinter.Label(text="is equal to", font=("Arial", 14,), padx=15)
is_equal.grid(column=0, row=1)

# Label
number = tkinter.Label(text="0", font=("Arial", 14,))
number.grid(column=1, row=1)

# Button
my_button = tkinter.Button(text='Calculate', command=button_clicked)
my_button.grid(column=1, row=2)

# Entry
miles_input = tkinter.Entry(width=10)
#print(userinput.get())

miles_input.grid(column=1, row=0)

window.mainloop()
