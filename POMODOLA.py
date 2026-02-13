BROWN = "#1F0318"
DEEP = "#09637E"
RED = "#B9C9BA"
ORANGE = "#E6501B"
WORKING_TIME = 45 # (Min)
BREAK_TIME = 5 # (Min)
REP = 0 #<--- TOTAL NUMBER OF WORKSESSION IS DONE, IF REP=4 TOTAL WORK SESSION DONE = 2 (WORK+REST)
timer = None
count_min = 0
count_sec = 0
marks = ""

import math

#---------------------------------------- TIMER RESET ----------------------------------------#
"""WHAT DOES RESET BUTTON DO?
    1. RESET TIMER TO 00:00
    2. RESET TEXT TO NORMAL TIMER
    3. RESET THE CHECKDOWN NUMBERS TO 0"""
def reset_timer():
    global timer
    global count_min
    global count_sec
    global marks
    global REP
    window.after_cancel(timer) # <-- after creating we have to push it in reset button using command
    title_label.config(text="Timer",font=("Century",50,"bold"),bg=RED,fg=BROWN)
    count_sec = 0
    count_min = 0
    canvas.itemconfig(timer_text,text=f"0{count_min}:0{count_sec}")
    marks = ""
    checkmark.config(text=marks)
    REP = 0
    
    

#---------------------------------------- TIMER MECHANISM ------------------------------------#
def start_timer():
    """ OUR GOAL 4 SET OF WORKING SET AND BETWEEN EACH SET
        5 MIN BREAK """
    global REP
    REP+=1
    WORK = 10*60
    SMALL_BREAK = 10*60
    LARGE_BREAK = 20*60

    # SET 2,4,6 SMALL BREAK 5 MIN
    if REP%2==0:
        title_label.config(text="TAKE A BREAK",font=("Cambria",50,"bold"),fg="#07AA12",)
        count_down(SMALL_BREAK)
        print(f"REP now is {REP} after {REP-1} REP of BREAK")

    # ATLAST 20 MIN LARGE BREAK
    elif REP%5==0:
        title_label.config(text="TAKE SOME REST",font=("Cambria",50,"bold"),fg="#F6CB0B",)
        count_down(LARGE_BREAK)
        print(f"Final REP BREAK is: {REP} ")
        
    else:
        # SET 1,3,5,7 WORKING SET OF 45 MIN
        title_label.config(text="BEAST MODE",font=("Cambria",50,"bold"),fg="#EB0909",)
        count_down(WORK)
        print(f"REP now is {REP} after {REP-1} REP of WORK")
        
#---------------------------------------- COUNTDOWN MECHANISM --------------------------------#
def count_down(count):
    global REP
    global timer
    global count_min
    global count_sec    
    count_min = math.floor(count/60)
    count_sec = count%60
    # Our focus is now handle "00:00"

    if count_min<10:
        count_min=f"0{count_min}"
    if count_sec==0:
        count_sec="00"
    elif count_sec<10:
        count_sec=f"0{count_sec}"
     
    canvas.itemconfig(timer_text,text=f"{count_min}:{count_sec}")
    if count>0:
        timer = window.after(1000,count_down,count-1)    # <---- TO CANCEL THE TIMER LATER WE HAVE TO PUT IT IN VARIABLE
        # AFTER CREATING TIMER, WE SEE THIS IS A LOCAL VARABLE BCZ IT IS UNDER A FUNCTION, SO WE HAVE TO MAKE IT A GLOBAL VARIABLE.
    else:
        start_timer()
        global marks
        marks = ""
        no_of_rep = math.floor(REP/2)
        for _ in range(no_of_rep):
            marks+="✓"
        checkmark.config(text=marks)

# NOW OUR MAIN WORK IS TO CHANGE TEXT 00:00 FROM CANVAS
#---------------------------------------- UI SETUP -------------------------------------------#


from tkinter import *

window = Tk()
window.title("LET'S TRY")
window.config(padx=10,pady=10,bg=RED)
# FOR COUNTDOWN WE HAVE A BUILTIN METHOD IN WINDOW--> AFTER()
# def countit(thing):
#     print(thing)
#     #thing-=1
# window.after(1000,countit,"Hello") #<--- for this we require millisec, func, *args


#TIMER NAME
title_label = Label(text="Timer",font=("Century",50,"bold"),bg=RED,fg=BROWN)
title_label.grid(row=1,column=2)

#LOGO
logo = PhotoImage(file="DAY-28/logo.png")
canvas = Canvas(width=640,height=640,bg=RED,highlightthickness=1)
canvas.create_image(320,320,image = logo)
timer_text = canvas.create_text(320,60,text="00:00",fill="White", font=("Cambria",50,"bold"))
canvas.grid(row=2,column=2)

#START-RESET
butt1 = Button(command=start_timer,text="Start",font=("Century",25,"bold"),bg=RED,fg=BROWN)
butt1.grid(row=3,column=1)

checkmark = Label(font=("Cambria",30),fg="black",bg=RED)
checkmark.grid(row=3,column=2)

butt2 = Button(text="Reset",font=("Century",25,"bold"),bg=RED,fg=BROWN,command=reset_timer)
butt2.grid(row=3,column=3)





window.mainloop()