from tkinter import *
import pandas as pd
import random

bg_color = "#B1DDC6"
data = pd.read_csv("french_words.csv")
data_dic = data.to_dict(orient="records")

def next_card():
    global choice,flip_timer
    choice = random.choice(data_dic)
    word=choice["French"]
    window.after_cancel(flip_timer)
    front_canvas.itemconfig(title_text,text="French" )
    front_canvas.itemconfig(word_text,text=f"{word}")
    # time= front_canvas.after(3000,trans_eng,eng_word)
    front_canvas.itemconfig(creat_img,image=front_img)
    flip_timer=window.after(3000,func=trans_eng)



def trans_eng():
    global choice
    front_canvas.itemconfig(creat_img, image=back_img)
    front_canvas.itemconfig(title_text,text="English" )
    front_canvas.itemconfig(word_text,text=choice["English"])
def is_known():
    data_dic.remove(choice)
    new_data = pd.DataFrame(data_dic)
    new_data.to_csv("word_to_learn.csv")
    next_card()
#............UI Setup.............
window = Tk()
window.title("Flashy")
window.config(padx=50,pady=50,bg=bg_color)
flip_timer =window.after(3000,func=trans_eng)


front_canvas = Canvas(width=800,height=526,highlightthickness=0)
front_img  = PhotoImage(file="card_front.png")
back_img = PhotoImage(file="card_back.png")
creat_img =front_canvas.create_image(400,263,image=front_img)
front_canvas.grid(column=0,row=0,columnspan=2)
front_canvas.config(bg=bg_color)
title_text = front_canvas.create_text(400,150,text="",font=("ariel",40, "italic"))
word_text = front_canvas.create_text(400,263,text="",font=("ariel",60,"bold"))

#button
img1 = PhotoImage(file="wrong.png")
button1 = Button(image=img1, highlightthickness=0, command=next_card)
button1.grid(column=0,row=1)
img2 = PhotoImage(file="right.png")

button2 = Button(image=img2, highlightthickness=0, command=is_known)
button2.grid(column=1,row=1)

next_card()




window.mainloop()