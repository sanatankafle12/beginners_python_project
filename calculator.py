from tkinter import *

exp = ""

def clicked(num):
    global exp
    exp = exp + str(num)
    equation.set(exp)

def equalclicked():
    try:
 
        global exp
        total = str(eval(exp))
 
        equation.set(total)
        exclickedion = ""
    except:
 
        equation.set(" error ")
        exclickedion = ""

def clear():
    global exp
    exp = ""
    equation.set("")
 
if __name__ == "__main__":
    window = Tk()
    window.geometry('300x250')
    window.title('calculator')
    window.configure(background='grey')

    equation = StringVar()
    equation_field = Entry(window,textvariable=equation).grid(column=1,row=0,pady=10)

    button1 = Button(window, text=' 1 ', fg='white', bg='black',
                    command=lambda: clicked(1), height=1, width=7)
    button1.grid(row=2, column=0)
 
    button2 = Button(window, text=' 2 ', fg='white', bg='black',
                    command=lambda: clicked(2), height=1, width=7)
    button2.grid(row=2, column=1)
 
    button3 = Button(window, text=' 3 ', fg='white', bg='black',
                    command=lambda: clicked(3), height=1, width=7)
    button3.grid(row=2, column=2)
 
    button4 = Button(window, text=' 4 ', fg='white', bg='black',
                    command=lambda: clicked(4), height=1, width=7)
    button4.grid(row=3, column=0)
 
    button5 = Button(window, text=' 5 ', fg='white', bg='black',
                    command=lambda: clicked(5), height=1, width=7)
    button5.grid(row=3, column=1)
 
    button6 = Button(window, text=' 6 ', fg='white', bg='black',
                    command=lambda: clicked(6), height=1, width=7)
    button6.grid(row=3, column=2)
 
    button7 = Button(window, text=' 7 ', fg='white', bg='black',
                    command=lambda: clicked(7), height=1, width=7)
    button7.grid(row=4, column=0)
 
    button8 = Button(window, text=' 8 ', fg='white', bg='black',
                    command=lambda: clicked(8), height=1, width=7)
    button8.grid(row=4, column=1)
 
    button9 = Button(window, text=' 9 ', fg='white', bg='black',
                    command=lambda: clicked(9), height=1, width=7)
    button9.grid(row=4, column=2)
 
    button0 = Button(window, text=' 0 ', fg='white', bg='black',
                    command=lambda: clicked(0), height=1, width=7)
    button0.grid(row=5, column=1)

    equal = Button(window, text=' = ', fg='white', bg='black',
                command=equalclicked, height=1, width=7)
    equal.grid(row=5, column=2)
 
    plus = Button(window, text=' + ', fg='white', bg='black',
                command=lambda: clicked("+"), height=1, width=7)
    plus.grid(row=2, column=6)
 
    minus = Button(window, text=' - ', fg='white', bg='black',
                command=lambda: clicked("-"), height=1, width=7)
    minus.grid(row=3, column=6)
 
    multiply = Button(window, text=' * ', fg='white', bg='black',
                    command=lambda: clicked("*"), height=1, width=7)
    multiply.grid(row=4, column=6)

 
    divide = Button(window, text=' / ', fg='white', bg='black',
                    command=lambda: clicked("/"), height=1, width=7)
    divide.grid(row=5, column=6)
 
 
    clear = Button(window, text='Reset', fg='white', bg='black',
                command=clear, height=2, width=14)
    clear.grid(row=6, column=1) 
    Decimal= Button(window, text='.', fg='white', bg='black',
                    command=lambda: clicked('.'), height=1, width=7)
    Decimal.grid(row=5,pady = 12)

    window.mainloop()