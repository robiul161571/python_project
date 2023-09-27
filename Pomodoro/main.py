from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 5
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None
# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(timer)
    title_label.config(text="Timer",fg=GREEN)
    canvas.itemconfig(timer_text,text="00:00")
    checkmark.config(text="")
    global reps
    reps =0
# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    global timer
    min = math.floor(count /60)
    sec = count %60
    if sec < 10:
        sec = f"0{sec}"
    canvas.itemconfig(timer_text,text=f"{min}:{sec}")
    if count > 0:
        timer = window.after(1000,count_down,count-1)
    else:
        start()
        marks = ""
        work_session = math.floor(reps/2)
        for _ in range(work_session):
            marks += "✔"
        checkmark.config(text=marks)

def start():
    global reps
    reps += 1

    if reps % 8 == 0:
        long_break = count_down(LONG_BREAK_MIN * 60)
        title_label.config(text="Break",fg=PINK,bg=YELLOW,highlightthickness=0,font=(FONT_NAME,50,"bold"))
    elif reps % 2 == 0:
        short_break = count_down(SHORT_BREAK_MIN * 60)
        title_label.config(text="Break",fg=RED,bg=YELLOW,highlightthickness=0,font=(FONT_NAME,50,"bold"))
    else:
        work_sec = count_down(WORK_MIN * 60)
        title_label.config(text="Work",fg=GREEN,bg=YELLOW,highlightthickness=0,font=(FONT_NAME,50,"bold"))


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100,pady=50,bg=YELLOW)

canvas = Canvas(width=200,height=224,bg=YELLOW,highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100,112,image=tomato_img)
timer_text = canvas.create_text(103,130,text="00:00", fill="white",font=(FONT_NAME,35,"bold"))
canvas.grid(column=2,row=2)

#label
title_label = Label(text="Timer",fg=GREEN,bg=YELLOW,highlightthickness=0,font=(FONT_NAME,50,"bold"))
title_label.grid(column=2,row=1)
checkmark = Label(text=" ",fg=GREEN,bg=YELLOW,highlightthickness=0,font=(35))
checkmark.grid(column=2,row=4)
#button
start_button = Button(text="Start",command=start)
start_button.grid(column=1,row=3)
reset_button = Button(text="Reset",command=reset_timer)
reset_button.grid(column=3,row=3)



window.mainloop()