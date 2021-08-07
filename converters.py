from tkinter import *
from tkinter import ttk

window = Tk()
window.geometry('200x200')
window.title('Converters..')

def binary_to_decimal():
    window.destroy()
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

def decimal_to_binary():
    window.destroy()

    def calculate(*args):
        try:
            num = int(decimal.get())
            binary_list = []
            while(num!=0):
                v = num%2
                binary_list.append(v)
                num = int(num/2)
            binary_list.reverse()
            solved = []
            for i in binary_list:
                i = str(i)
                solved.append(i)

            binary.set("".join(solved))
        except:
            binary.set("Invalid..")
    

    root = Tk()
    root.title("Decimal to Binary")

    mainframe = ttk.Frame(root, padding="3 3 12 12")
    mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)

    decimal = StringVar()
    decimal_entry = ttk.Entry(mainframe, width=7, textvariable=decimal)
    decimal_entry.grid(column=2, row=1, sticky=(W, E))


    binary = StringVar()
    ttk.Label(mainframe, textvariable=binary).grid(column=2, row=2, sticky=(W, E))

    ttk.Button(mainframe, text="Calculate", command=calculate).grid(column=3, row=3, sticky=W)


    ttk.Label(mainframe, text="Decimal").grid(column=3, row=1, sticky=W)
    ttk.Label(mainframe, text="is equivalent to").grid(column=1, row=2, sticky=E)
    ttk.Label(mainframe, text="Binary").grid(column=3, row=2, sticky=W)


    for child in mainframe.winfo_children(): 
        child.grid_configure(padx=5, pady=5)

    decimal_entry.focus()
    root.mainloop()


my_button = Button(text = 'Binary to decimal',command=binary_to_decimal)
my_button.pack()

my_button1 = Button(text = 'decimal_to_binary',command=decimal_to_binary)
my_button1.pack()

window.mainloop()