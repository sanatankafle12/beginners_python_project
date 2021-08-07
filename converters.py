from tkinter import *
from tkinter import ttk

window  = Tk()
window.geometry('100x100')
window.title('Converters..')

def calculate(*args):
    s = 0
    n = 0
    num = binary.get()
    length = len(num)
    for i in num:
        if i == '0' or i == '1':
            num = int(num)
            while num!=0:
                v = num%10
                to_add = v*pow(2,n)
                n+=1
                s+=to_add
                num = int(num/10)
        else:
            decimal.set('Invalid..')   
            break
    if n == length:
        decimal.set(s)
        
def binary_tkinter():
    window.destroy()
    root = Tk()
    root.title("Binary To Decimal")

    mainframe = ttk.Frame(root, padding="3 3 12 12")
    mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)

    binary = StringVar()
    binary_entry = ttk.Entry(mainframe, width=7, textvariable=binary)
    binary_entry.grid(column=2, row=1, sticky=(W, E))


    decimal = StringVar()
    ttk.Label(mainframe, textvariable=decimal).grid(column=2, row=2, sticky=(W, E))

    ttk.Button(mainframe, text="Calculate", command=calculate).grid(column=3, row=3, sticky=W)


    ttk.Label(mainframe, text="Binary").grid(column=3, row=1, sticky=W)
    ttk.Label(mainframe, text="is equivalent to").grid(column=1, row=2, sticky=E)
    ttk.Label(mainframe, text="Decimal").grid(column=3, row=2, sticky=W)


    for child in mainframe.winfo_children(): 
        child.grid_configure(padx=5, pady=5)

    binary_entry.focus()
    root.mainloop()


my_button = Button(text="Binary_to_decimal", command=binary_tkinter)
my_button.pack()

window.mainloop()