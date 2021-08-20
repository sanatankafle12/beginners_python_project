from tkinter import *
from gtts import gTTS
from playsound import playsound


window = Tk()
window.geometry('400x400')
window.title('Convert text into speech!!!')


Label(window,text ="Enter Text to Hear", font = 'arial 15 bold', bg ='white smoke').place(x=20,y=60)

text_message = StringVar()

space = Entry(window,textvariable = text_message,width = '50')
space.place(x= 20,y=100)

def Text_to_speech():
    Message = space.get()
    speech = gTTS(text = Message)
    speech.save('output.mp3')

def play():
    playsound('output.mp3')

def Exit():
    window.destroy()


Button(window, text = "Convert", command = Text_to_speech ,width = '7').place(x=25,y=140)

Button(window, text = "Play", command = play ,width = '4').place(x=100,y=140)

Button(window,text = 'EXIT', width = '4' , command = Exit).place(x=150 , y = 140)


window.mainloop()