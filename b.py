import pyttsx3
from tkinter import *
import time
pol=Tk()
p=pyttsx3.init ()
p.say('hello sir! my name is jarvis')
p.runAndWait()

pol.geometry('890x600')
h=Label(pol,text='Jarvis',font='Arial 22 bold')
h.place(x=330,y=0)
m=Entry(pol,width=455,font='Arial 25 bold')
m.place(x=0,y=60)

def pl():
    if m.get()=='hi':
        p.say('hello sir')
        p.runAndWait()
    if m.get()=='time':
        p.say(time.strftime('%H:%M'))
        p.runAndWait()
b=Button(pol,text='Say',bg='blue',fg='white',command=pl,width=21)
b.place(x=350,y=100)

pol.mainloop()
