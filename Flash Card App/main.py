import pandas
from tkinter import *
import random

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}


data = pandas.read_csv("c:/Users/ANKIT/Desktop/Working with Tkinter/Flash Card App/data/french_words.csv")
to_learn = data.to_dict(orient="records")

def generate_new_card():
    global current_card
    global flip_timer

    window.after_cancel(flip_timer)


    current_card = random.choice(to_learn)

    canvas.itemconfig(card_title, text="French",fill='black')
    canvas.itemconfig(card_word, text= current_card['French'],fill='black')
    canvas.itemconfig(canvas_image, image=front_image)

    flip_timer = window.after(3000, flip_card)


def flip_card():
    english_card = current_card["English"]

    canvas.itemconfig(canvas_image, image=back_image)
    canvas.itemconfig(card_title, text=current_card['English'],fill='white')
    canvas.itemconfig(card_word, text=english_card, fill='white')

def is_known():
    global current_card
    to_learn.remove(current_card)

    data = pandas.DataFrame(to_learn)

    data.to_csv("c:/Users/ANKIT/Desktop/py100/day31/words_to_learn.csv")

    generate_new_card()




window = Tk()
window.title("My Flash Card App")
window.config(bg=BACKGROUND_COLOR)
window.config(padx=50, pady=50)

canvas = Canvas(width=800, height=526)

front_image = PhotoImage(file="c:/Users/ANKIT/Desktop/py100/day31/images/card_front.png")
back_image = PhotoImage(file="c:/Users/ANKIT/Desktop/py100/day31/images/card_back.png")

canvas_image = canvas.create_image(400, 263, image=front_image)
canvas.grid(row=0, column=0,columnspan=2)
canvas.config(bg=BACKGROUND_COLOR,highlightthickness=0)

card_title = canvas.create_text(400,150, text="", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400,263, text="", font=("Ariel", 60, "bold"))

right_img = PhotoImage(file="c:/Users/ANKIT/Desktop/py100/day31/images/right.png")
wrong_img = PhotoImage(file="c:/Users/ANKIT/Desktop/py100/day31/images/wrong.png")

right_button = Button(image=right_img, highlightthickness=0,command=is_known)
right_button.grid(row=1,column=1)

wrong_button = Button(image=wrong_img, highlightthickness=0,command=generate_new_card)
wrong_button.grid(row=1,column=0)


flip_timer = window.after(3000,flip_card)

window.mainloop()
