import tkinter
from PIL import Image, ImageTk
import random


#here root window has been created with the given dimension and title.
root = tkinter.Tk()
root.geometry('800x800')
root.title('Welcome To the roller!!!')


# images which represent sides to the dice are added to a list to use them randomly.
dice = ['dice1.png', 'dice2.png', 'dice3.png', 'dice4.png', 'dice5.png', 'dice6.png']


# #choosing a random dice
image1 = ImageTk.PhotoImage(Image.open(random.choice(dice)))

# # making a label for images
label1 = tkinter.Label(root, image=image1)
label1.image = image1
label1.pack( expand=True)



#Function that gets called when the roll button is pressed
def rolling_dice():
    image1 = ImageTk.PhotoImage(Image.open(random.choice(dice)))
    label1.configure(image=image1)
    label1.image = image1


#adding photo to the button (Not necessary, can use other ways to create the button.)
Photo = ImageTk.PhotoImage(file =r"button.png")
button = tkinter.Button(root, image = Photo, command=rolling_dice).pack(expand=True)

root.mainloop()