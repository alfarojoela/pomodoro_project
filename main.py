from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

reps= 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    timer_label.config(text="Timer")
    check_marks.config(text="")
    global reps
    reps = 0




# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60


    #if it's the 8th rep:

    if reps % 8 == 0:
        count_down(long_break_sec)
        timer_label.config(text="Break", fg=RED)

     #if it's the 2nd/4th/6th rep:
    elif reps %2 == 0:
        count_down(short_break_sec)
        timer_label.config(text="Break", fg=PINK)

    #if it's the 1st/3rd/5th/7th rep:
    else:
        count_down(work_sec)
        timer_label.config(text="Work", fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60

    if count_sec < 10:
        count_sec = f"0{count_sec}"


    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count-1)
    else:
        start_timer()
        mark ="✓"
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            mark += ""
        check_marks.config(text=mark)





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
timer_text=canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold")) #default text, color is white
#FONT_NAME is above constant

canvas.grid(row=1, column =1)  #appears to center canvas.

#count_down(5)

#command needs to be set to the name of the function to trigger
start_button = Button(text="Start",highlightthickness=0, font=(FONT_NAME, 12), command=start_timer)
start_button.grid(column=0, row=2) #original row value was 5. doesn't seem much different

reset_button = Button(text="Reset",highlightthickness=0, command=reset_timer, font=(FONT_NAME, 12))
reset_button.grid(column = 3, row=2)

check_marks = Label(text="", fg=GREEN, bg=YELLOW, font=(100))
check_marks.grid(column=1, row=3)

















window.mainloop()