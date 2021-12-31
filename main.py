from tkinter import *
import requests

FONT = ("Open Sans", 20)


def get_quote():
    response = requests.get('https://api.kanye.rest/')
    response.raise_for_status()
    quote = response.json()['quote']
    canvas.itemconfig(quote_text, text=quote)


root = Tk()
root.title("Kanye Says...")
root.wm_iconbitmap('kanye.ico')
root.config(padx=50, pady=50)

canvas = Canvas(root, width=300, height=414)
background_img = PhotoImage(file="background.png")
canvas.create_image(150, 207, image=background_img)
quote_text = canvas.create_text(150, 207, text="Click me to hear what I gotta say...",
                                width=250, font=FONT, fill="white")
canvas.grid(row=0, column=0)

kanye_img = PhotoImage(file="kanye.png")
kanye_button = Button(image=kanye_img, borderwidth=0, command=get_quote)
kanye_button.grid(row=1, column=0)

root.mainloop()