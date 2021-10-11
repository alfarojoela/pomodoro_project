from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
import time




# ---------------------------- UI SETUP ------------------------------- #

# order of object placement in window appears to affect how grid arguments are set up.
# grid placement is in relation to other object placement.  arguments are not absolute positions.
#current solution put timer label in first.  then canvas then buttons.
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

#fg argument sets color foreground for label text

timer_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50))
timer_label.grid(row=0, column=1) # this centers it in the window.  not sure why?  expected row=0, column = 1




canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0) #last argument not well documented.  gets rid
#of small white square border around image.


tomato_img= PhotoImage(file="tomato.png")  #this function needs file path
canvas.create_image(100, 112, image=tomato_img) #x position is 100, y position is 112 image as argument points to variable name
canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold")) #default text, color is white
#FONT_NAME is above constant

canvas.grid(row=1, column =1)  #appears to center canvas.

start_button = Button(text="Start",highlightthickness=0, font=(FONT_NAME, 12))
start_button.grid(column=0, row=2) #original row value was 5. doesn't seem much different

reset_button = Button(text="Reset",highlightthickness=0, font=(FONT_NAME, 12))
reset_button.grid(column = 3, row=2)

check_marks = Label(text="✓", fg=GREEN, bg=YELLOW, font=(100))
check_marks.grid(column=1, row=3)

















window.mainloop()