from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
# We declare it as global so that we can simulaneously switch between its French and English Translation
current_card = {}
# We declare it as global so that we can access it to perform various operations on it like accessing,deleting etc
to_learn = {}

try:
    # First we try and see if words_to_learn file exists
    data = pandas.read_csv("c:/Users/ANKIT/Desktop/Working with Tkinter/Flash Card App/data/words_to_learn.csv")
except FileNotFoundError:
    # If the file is not found, we start by accessing words form the original file of french_words
    original_data = pandas.read_csv("c:/Users/ANKIT/Desktop/Working with Tkinter/Flash Card App/data/french_words.csv")
    print(original_data)
    to_learn = original_data.to_dict(orient="records")
else:
    # Orient converts our csv data into column -> value list form where each French word word will have its English translation
    # If the words_to_learn file exists we access French words from it
    to_learn = data.to_dict(orient="records")


def next_card():
    global current_card, flip_timer

    # Stops the flipping of card until we wait on a card word for 3 seconds
    window.after_cancel(flip_timer)

    # To pick a random french word and display on card
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    canvas.itemconfig(card_background, image=card_front_img)

    flip_timer = window.after(3000, func=flip_card)

# To show the card with English translation of the word
def flip_card():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(card_background, image=card_back_img)


def is_known():
    # Remove the word from the french_words file 
    to_learn.remove(current_card)
    # print(len(to_learn))

    # Creating new file of words from original file where removed words don't exist
    data = pandas.DataFrame(to_learn)
    # index = False is used to stop it from adding index values to word
    data.to_csv("c:/Users/ANKIT/Desktop/Working with Tkinter/Flash Card App/data/words_to_learn.csv", index=False)

    # Showing the user new card to guess
    next_card()


window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# To flip the card after 3 seconds we create a function called flip_card to flip to English card translation
flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=526)

# To set image for French card
card_front_img = PhotoImage(file="c:/Users/ANKIT/Desktop/Working with Tkinter/Flash Card App/images/card_front.png")
# To set image for English card
card_back_img = PhotoImage(file="c:/Users/ANKIT/Desktop/Working with Tkinter/Flash Card App/images/card_back.png")

card_background = canvas.create_image(400, 263, image=card_front_img)

card_title = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))

canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

# This displays the new card word on screen to learn
cross_image = PhotoImage(file="c:/Users/ANKIT/Desktop/Working with Tkinter/Flash Card App/images/wrong.png")
unknown_button = Button(image=cross_image, highlightthickness=0, command=next_card)
unknown_button.grid(row=1, column=0)

# This is used to checkmark that the user already knows the word and should not be asked again
check_image = PhotoImage(file="c:/Users/ANKIT/Desktop/Working with Tkinter/Flash Card App/images/right.png")
known_button = Button(image=check_image, highlightthickness=0, command=is_known)
known_button.grid(row=1, column=1)

# TO directly start by displaying the first French word card
next_card()

window.mainloop()



