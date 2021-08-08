from tkinter import *
from tkinter import ttk

window = Tk()
window.geometry('500x500')
window.title('Converters..')

#Change binary to decimal
def btod(num):
        s = 0
        n = 0
        length = len(num)
        if length == 1 and (num == '1' or num == '0'):
            s = num
            return s
            
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
                return 1 
                break
        if n == length:
            return s

#change decimal to binary
def dtob(num):
        try:
            num = int(num)
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

            binary_string = "".join(solved)
            return binary_string
        except:
            return 1

#to add ui for binary to decimal conversion 
def binary_to_decimal():
    def calculate():

        if btod(binary.get()) == 1:
            decimal.set('Invalid..')
        else:
            decimal.set(btod(binary.get()))
            
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

#to add ui to decimal to binary convertor
def decimal_to_binary():
    window.destroy()

    def calculate():
        if dtob(decimal.get()) == 1:
            binary.set('Invalid ...')
        else:
            binary.set(dtob(decimal.get()))

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


#to add gui and also make two binary numbers added
def binary_adder():

    def calculate():

        if btod(binary.get()) == 1 or btod(binary1.get()) == 1:
            total.set('Invalid ..')
        else:
            num_1 = int(btod(binary.get()))
            num_2 = int(btod(binary1.get()))
            decimal = num_1 + num_2
            if dtob(decimal) == 1:
                total.set('Invalid ...')
            else:
                total.set(dtob(decimal))
        

    window.destroy()
    root = Tk()
    root.title("Binary Adder")

    mainframe = ttk.Frame(root, padding="3 3 12 12")
    mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)

    binary = StringVar()
    binary_entry = ttk.Entry(mainframe, width=7, textvariable=binary)
    binary_entry.grid(column=2, row=1, sticky=(W, E))

    binary1 = StringVar()
    binary1_entry = ttk.Entry(mainframe, width=7, textvariable=binary1)
    binary1_entry.grid(column=2, row=2, sticky=(W, E))


    total = StringVar()

    ttk.Label(mainframe, textvariable=total).grid(column=2, row=3, sticky=(W, E))

    ttk.Button(mainframe, text="Calculate", command=calculate).grid(column=3, row=4, sticky=W)

    ttk.Label(mainframe, text="Binary1").grid(column=3, row=1, sticky=W)
    ttk.Label(mainframe, text="Binary2").grid(column=3, row=2, sticky=W)
    ttk.Label(mainframe, text="Sum").grid(column=3, row=3, sticky=W)


    for child in mainframe.winfo_children(): 
        child.grid_configure(padx=5, pady=5)

    binary_entry.focus()
    binary1_entry.focus()
    root.mainloop()

#to substract two binary numbers
def binary_substraction():

    def calculate():

        if btod(binary.get()) == 1 or btod(binary1.get()) == 1:
            total.set('Invalid ..')
        else:
            num_1 = int(btod(binary.get()))
            num_2 = int(btod(binary1.get()))
            decimal = num_1 - num_2
            if dtob(decimal) == 1:
                total.set('Invalid ...')
            else:
                total.set(dtob(decimal))
        

    window.destroy()
    root = Tk()
    root.title("Binary Adder")

    mainframe = ttk.Frame(root, padding="3 3 12 12")
    mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)

    binary = StringVar()
    binary_entry = ttk.Entry(mainframe, width=7, textvariable=binary)
    binary_entry.grid(column=2, row=1, sticky=(W, E))

    binary1 = StringVar()
    binary1_entry = ttk.Entry(mainframe, width=7, textvariable=binary1)
    binary1_entry.grid(column=2, row=2, sticky=(W, E))


    total = StringVar()

    ttk.Label(mainframe, textvariable=total).grid(column=2, row=3, sticky=(W, E))

    ttk.Button(mainframe, text="Calculate", command=calculate).grid(column=3, row=4, sticky=W)

    ttk.Label(mainframe, text="Binary1").grid(column=3, row=1, sticky=W)
    ttk.Label(mainframe, text="Binary2").grid(column=3, row=2, sticky=W)
    ttk.Label(mainframe, text="Difference").grid(column=3, row=3, sticky=W)


    for child in mainframe.winfo_children(): 
        child.grid_configure(padx=5, pady=5)

    binary_entry.focus()
    binary1_entry.focus()
    root.mainloop()


#to add buttons to the main window and make them open new windows 
def main_window():
    
    my_button = Button(text = 'Binary to decimal',command=binary_to_decimal)
    my_button.pack(pady=15)

    my_button1 = Button(text = 'decimal_to_binary',command=decimal_to_binary)
    my_button1.pack(pady=15)

    my_button2 = Button(text = 'binary adder',command = binary_adder)
    my_button2.pack(pady=15)

    my_button2 = Button(text = 'binary substractor',command = binary_substraction)
    my_button2.pack(pady=15)

    window.mainloop()


if __name__ == "__main__":
    main_window()