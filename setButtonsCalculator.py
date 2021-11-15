from tkinter import *
from typing import Collection
from functionsCalculator.functions import Functions

root = Tk()
myFrame = Frame(root)

myFrame.pack()
#Create the object 
functions_pack = Functions()

# operation:str = ""
# result = 0
# # --------------------Screen--------------------------
# screenNumber = StringVar()
screen = Entry(myFrame, textvariable=functions_pack.screenNumber)
screen.grid(row=1, column=1, padx=5, pady=5, columnspan=4)

screen.config(background="black", fg="#03f943", justify="right")

# #----------------------------pulsaciones teclado-----------

# def numeroPulsado(num: str):
#     global operation

#     if operation != "":
#         screenNumber.set(num)
#         operation = ""
#     else:
#         screenNumber.set(screenNumber.get() + num)
        
# #-----------------------función suma-----------------------
# def suma(num):
#     global operation
#     global result
#     result += int(num)
#     operation = "suma"
#     screenNumber.set(result)

# #------------Función el_resultado----------------------------
# def el_resultado():
#     global result
#     screenNumber.set(result + int(screenNumber.get()))

#     result = 0


#-------------------Fila 1----------------------------------

button_7 = Button(myFrame, text="7", pady=10, width=3, command=lambda:functions_pack.numeroPulsado("7"))
button_7.grid(row=2, column=1)
button_8 = Button(myFrame, text="8", pady=10, width=3, command=lambda:functions_pack.numeroPulsado("8"))
button_8.grid(row=2, column=2)
button_9 = Button(myFrame, text="9", pady=10, width=3, command=lambda:functions_pack.numeroPulsado("9"))
button_9.grid(row=2, column=3)
button_div = Button(myFrame, text="/", pady=10, width=3)
button_div.grid(row=2, column=4)

#-------------------Fila 2----------------------------------

button_4 = Button(myFrame, text="4", pady=10, width=3, command=lambda:functions_pack.numeroPulsado("4"))
button_4.grid(row=3, column=1)
button_5 = Button(myFrame, text="5", pady=10, width=3, command=lambda:functions_pack.numeroPulsado("5"))
button_5.grid(row=3, column=2)
button_6 = Button(myFrame, text="6", pady=10, width=3, command=lambda:functions_pack.numeroPulsado("6"))
button_6.grid(row=3, column=3)
button_mult = Button(myFrame, text="X", pady=10, width=3)
button_mult.grid(row=3, column=4)

#-------------------Fila 3----------------------------------

button_1 = Button(myFrame, text="1", pady=10, width=3, command=lambda:functions_pack.numeroPulsado("1"))
button_1.grid(row=4, column=1)
button_2 = Button(myFrame, text="2", pady=10, width=3, command=lambda:functions_pack.numeroPulsado("2"))
button_2.grid(row=4, column=2)
button_3 = Button(myFrame, text="3", pady=10, width=3, command=lambda:functions_pack.numeroPulsado("3"))
button_3.grid(row=4, column=3)
button_rest = Button(myFrame, text="-", pady=10, width=3, command=lambda:functions_pack.sustraction(functions_pack.screenNumber.get()))
button_rest.grid(row=4, column=4)

#-------------------Fila 4----------------------------------

button_dot = Button(myFrame, text=".", pady=10, width=3)
button_dot.grid(row=5, column=1)
button_0 = Button(myFrame, text="0", pady=10, width=3, command=lambda:functions_pack.numeroPulsado("0"))
button_0.grid(row=5, column=2)
button_equals = Button(myFrame, text="=", pady=10, width=3, command=lambda:functions_pack.el_resultado())
button_equals.grid(row=5, column=3)
button_sum = Button(myFrame, text="+", pady=10, width=3, command=lambda:functions_pack.suma(functions_pack.screenNumber.get()))
button_sum.grid(row=5, column=4)

#-------función aparición de números en pantalla al presionarlos--------


if __name__ == "__main__":

    root.mainloop()
