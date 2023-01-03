import os
os.system('cls')

from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "ArialRounded"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 

def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    checkmark.config(text="")

# ---------------------------- TIMER STOP ------------------------------- # 
def stop_timer():

    window.after_cancel(timer)
    


# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if lg_break():
        count_down(long_break_sec)
    elif sh_break():
        count_down(short_break_sec)
    else:
        count_down(work_sec)
        

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def count_down(count):

    count_min = math.floor(count / 60)
    count_sec = count % 60

    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        
        marks = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            marks += "✔"

        checkmark.config(text=marks)
        


def pomodoro():
    canvas.itemconfig(timer_text, text="25:00")

def sh_break():
    canvas.itemconfig(timer_text, text="5:00")

def lg_break():
    canvas.itemconfig(timer_text, text="20:00")

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("PomoFocus")
window.config(padx=100, pady=50, bg=YELLOW)

# Timer Label
# timer_label = Label(text="Timer", font=(FONT_NAME, 50, "bold" ), fg=GREEN, bg=YELLOW)
# timer_label.grid(row=0,column=1)

# Pomodoro Timer Start
pomodoro = Button(text="Pomodoro", font= (FONT_NAME, 20, "bold"), highlightthickness=0,command=pomodoro)
pomodoro.grid(row=0,column=0)

# Start short break
short_break = Button(text="Short Break", font= (FONT_NAME, 20, "bold"), highlightthickness=0,command=sh_break)
short_break.grid(row=0,column=1)

# Start long break
long_break = Button(text="Long Break",font= (FONT_NAME, 20, "bold"), highlightthickness=0,command=lg_break)
long_break.grid(row=0,column=2)

# Creating a Canvas
canvas = Canvas(width=200, height=224, bg=YELLOW,highlightthickness=0)
# PhotoImage is a method in Tkinter to get hold of an image file in a particular location
tomato_img = PhotoImage(file="c:/Users/ANKIT/Desktop/Working with Tkinter/Pomodoro TImer/tomato.png")
canvas.create_image(100, 112, image=tomato_img)

# To place text on the canvas 
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font= (FONT_NAME, 35, "bold"))

canvas.grid(row=1, column=1)


# Start Button
start = Button(text="START", font= (FONT_NAME, 20, "bold"), highlightthickness=0,command=start_timer)
start.grid(row=2,column=0)

# Stop Button
stop = Button(text="STOP", font= (FONT_NAME, 20, "bold"), highlightthickness=0,command=stop_timer)
stop.grid(row=2,column=1)

# Reset Button
reset = Button(text="RESET",font= (FONT_NAME, 20, "bold"), highlightthickness=0,command=reset_timer)
reset.grid(row=2,column=2)

# Checkmark Label
checkmark = Label(fg=GREEN, bg=YELLOW, font=("bold"))
checkmark.grid(row=4,column=1)

window.mainloop()