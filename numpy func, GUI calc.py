add func*

# numpy.add() function
# when inputs are scalar
  
import numpy as geek
in_num1 = 10
in_num2 = 15
  
print ("1st Input  number : ", in_num1)
print ("2nd Input  number : ", in_num2)
    
out_num = geek.add(in_num1, in_num2) 
print ("output number after addition  : ", out_num)


slicing*

import numpy as np

a = np.array([2, 4, 6, 8])
print(a)
b = a[:3]
print(b)

shape*

import numpy as np

arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
print(arr.shape)


reshape*

import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
newarr = arr.reshape(4, 3)
print(newarr)


Printing specific element*

import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7])
print(arr[0])


delete*

import numpy as np
a = ([1,2,3,4])
print(a)
#  a - it is an array and 0 is the index 
a = np.delete(a,0)
print(a)



GUI calculator*

import tkinter as tk
import tkinter.messagebox
from tkinter.constants import SUNKEN

window = tk.Tk()
frame = tk.Frame(master=window, bg="lightgreen", padx=10)
frame.pack()
entry = tk.Entry(master=frame, relief=SUNKEN, borderwidth=3, width=30)
entry.grid(row=0, column=0, columnspan=3, ipady=2, pady=2)


def myclick(number):
    entry.insert(tk.END, number)


def equal():
    try:
        y = str(eval(entry.get()))
        entry.delete(0, tk.END)
        entry.insert(0, y)
    except:
        tkinter.messagebox.showinfo("Error", "Syntax Error")


def clear():
    entry.delete(0, tk.END)


button_1 = tk.Button(master=frame, text='1', padx=15,
                     pady=5, width=3, command=lambda: myclick(1))
button_1.grid(row=1, column=0, pady=2)
button_2 = tk.Button(master=frame, text='2', padx=15,
                     pady=5, width=3, command=lambda: myclick(2))
button_2.grid(row=1, column=1, pady=2)
button_3 = tk.Button(master=frame, text='3', padx=15,
                     pady=5, width=3, command=lambda: myclick(3))
button_3.grid(row=1, column=2, pady=2)
button_4 = tk.Button(master=frame, text='4', padx=15,
                     pady=5, width=3, command=lambda: myclick(4))
button_4.grid(row=2, column=0, pady=2)
button_5 = tk.Button(master=frame, text='5', padx=15,
                     pady=5, width=3, command=lambda: myclick(5))
button_5.grid(row=2, column=1, pady=2)
button_6 = tk.Button(master=frame, text='6', padx=15,
                     pady=5, width=3, command=lambda: myclick(6))
button_6.grid(row=2, column=2, pady=2)
button_7 = tk.Button(master=frame, text='7', padx=15,
                     pady=5, width=3, command=lambda: myclick(7))
button_7.grid(row=3, column=0, pady=2)
button_8 = tk.Button(master=frame, text='8', padx=15,
                     pady=5, width=3, command=lambda: myclick(8))
button_8.grid(row=3, column=1, pady=2)
button_9 = tk.Button(master=frame, text='9', padx=15,
                     pady=5, width=3, command=lambda: myclick(9))
button_9.grid(row=3, column=2, pady=2)
button_0 = tk.Button(master=frame, text='0', padx=15,
                     pady=5, width=3, command=lambda: myclick(0))
button_0.grid(row=4, column=1, pady=2)

button_add = tk.Button(master=frame, text="+", padx=15,
                       pady=5, width=3, command=lambda: myclick('+'))
button_add.grid(row=5, column=0, pady=2)

button_subtract = tk.Button(
    master=frame, text="-", padx=15, pady=5, width=3, command=lambda: myclick('-'))
button_subtract.grid(row=5, column=1, pady=2)

button_multiply = tk.Button(
    master=frame, text="*", padx=15, pady=5, width=3, command=lambda: myclick('*'))
button_multiply.grid(row=5, column=2, pady=2)

button_div = tk.Button(master=frame, text="/", padx=15,
                       pady=5, width=3, command=lambda: myclick('/'))
button_div.grid(row=6, column=0, pady=2)

button_clear = tk.Button(master=frame, text="clear",
                         padx=15, pady=5, width=12, command=clear)
button_clear.grid(row=6, column=1, columnspan=2, pady=2)

button_equal = tk.Button(master=frame, text="=", padx=15,
                         pady=5, width=9, command=equal)
button_equal.grid(row=7, column=0, columnspan=3, pady=2)

window.mainloop()

