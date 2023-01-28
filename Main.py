import time
import tkinter as tk
from tkinter import *
from datetime import datetime
from win10toast import ToastNotifier
import winsound

#creating a winodw
window = Tk()
window.geometry('600x600')#giving size
window.title('PythonGeeks')#giving title
Label(window, text="Countdown Clock and Timer", font=('Calibri 15')).pack(pady=20)

#to print current time
now = datetime.now()
current_time = now.strftime("%H:%M:%S")
Label(window,text=current_time).pack()

check=tk.BooleanVar()#check is of boolean type
hour=tk.IntVar()# ensure count is of integer type
minus=tk.IntVar()# ensure count is of integer type
secon=tk.IntVar()# ensure count is of integer type
# define the countdown func.
def countdown():
    h=hour.get()#get the value
    m=minus.get()#get the value
    s=secon.get()#get the value
    t= h * 3600 + m * 60 + s
    while t:
        mins, secs = divmod(t, 60)
        display = ('{:02d}:{:02d}'.format(mins, secs))
        time.sleep(1)#sleep time 1 sec
        t -= 1
        Label(window,text= display).pack()
    
    if (check.get()==True):#if the value of check is true     
            winsound.Beep(440, 1000)#beep sound 
        
    Label(window,text="Time-Up",font=('bold', 20)).place(x=250,y=440)
    #display notification on dekstop
    toast = ToastNotifier()#create toast variable
    toast.show_toast("Notification","Timer is Off",duration = 20,icon_path = NONE,threaded = True,)#show toast


Label(window,text="Enter time in HH:MM:SS",font=('bold')).pack()
Entry(window,textvariable = hour,width=30).pack()

Entry(window,textvariable = minus,width=30).pack()

Entry(window,textvariable = secon,width=30).pack()

Checkbutton(text='Check for Music',onvalue=True,variable=check).pack()#creating checkbox
Button(window,text="Set Countdown",command=countdown,bg='yellow').pack()#create buttons  
window.update()#update the window
window.mainloop()#main command