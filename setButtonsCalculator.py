from tkinter import *
from typing import Collection
from functionsCalculator.functions import Functions
class Calculator():
    def __init__(self):
        root = Tk()
        root.title("Basic Calculator")
        root.iconbitmap("perfil.ico")
        myFrame = Frame(root)

        myFrame.pack()
        #Create the object 
        functions_pack = Functions()
        # # --------------------Screen--------------------------
        screen = Entry(myFrame, textvariable=functions_pack.screen_number)
        screen.grid(row=0, column=1, padx=5, pady=5, columnspan=6, sticky= W + E)

        screen.config(background="black", fg="#03f943", justify="right")

        #-------------------Row 1----------------------------------

        mor_less_button = Button(myFrame, text= '+/-', pady=10, width=3, command=lambda:functions_pack.negative_or_positive_number())
        mor_less_button.grid(row=2, column=1)
        button_7 = Button(myFrame, text="7", pady=10, width=3, command=lambda:functions_pack.number_pressed("7"))
        button_7.grid(row=2, column=2)
        button_8 = Button(myFrame, text="8", pady=10, width=3, command=lambda:functions_pack.number_pressed("8"))
        button_8.grid(row=2, column=3)
        button_9 = Button(myFrame, text="9", pady=10, width=3, command=lambda:functions_pack.number_pressed("9"))
        button_9.grid(row=2, column=4)
        percentage_button = Button(myFrame, text="%", pady=10, width=3, command=lambda:functions_pack.percentage())
        percentage_button.grid(row=2, column=5)
        square_root_button = Button(myFrame, text="√", pady=10, width=3, command=lambda:functions_pack.square_root())
        square_root_button.grid(row=2, column=6)


        #-------------------Row 2----------------------------------

        arrow_button = Button(myFrame, text="◀", pady=10, width=3, command=lambda:functions_pack.delete_last_number())
        arrow_button.grid(row=3, column=1)
        button_4 = Button(myFrame, text="4", pady=10, width=3, command=lambda:functions_pack.number_pressed("4"))
        button_4.grid(row=3, column=2)
        button_5 = Button(myFrame, text="5", pady=10, width=3, command=lambda:functions_pack.number_pressed("5"))
        button_5.grid(row=3, column=3)
        button_6 = Button(myFrame, text="6", pady=10, width=3, command=lambda:functions_pack.number_pressed("6"))
        button_6.grid(row=3, column=4)
        button_mult = Button(myFrame, text="X", pady=10, width=3, command=lambda:functions_pack.multiplication(functions_pack.screen_number.get()))
        button_mult.grid(row=3, column=5)
        button_div = Button(myFrame, text="÷", pady=10, width=3, command=lambda:functions_pack.division(functions_pack.screen_number.get()))
        button_div.grid(row=3, column=6)

        #-------------------Row 3----------------------------------

        clear_button = Button(myFrame, text="C", pady=10, width=3, command=lambda:functions_pack.clear_screen())
        clear_button.grid(row=4, column=1)
        button_1 = Button(myFrame, text="1", pady=10, width=3, command=lambda:functions_pack.number_pressed("1"))
        button_1.grid(row=4, column=2)
        button_2 = Button(myFrame, text="2", pady=10, width=3, command=lambda:functions_pack.number_pressed("2"))
        button_2.grid(row=4, column=3)
        button_3 = Button(myFrame, text="3", pady=10, width=3, command=lambda:functions_pack.number_pressed("3"))
        button_3.grid(row=4, column=4)
        button_rest = Button(myFrame, text="-", pady=10, width=3, command=lambda:functions_pack.subtraction(functions_pack.screen_number.get()))
        button_rest.grid(row=4, column=6)

        #---------------------Row 4---------------------------------

        ac_button = Button(myFrame, text="AC", pady=10, width=3, command=lambda:functions_pack.clear_all())
        ac_button.grid(row=5, column=1)
        button_0 = Button(myFrame, text="0", pady=10, width=3, command=lambda:functions_pack.number_pressed("0"))
        button_0.grid(row=5, column=2)
        button_double0 = Button(myFrame, text="00", pady=10, width=3, command=lambda:functions_pack.number_pressed("00"))
        button_double0.grid(row=5, column=3)
        button_dot = Button(myFrame, text=".", pady=10, width=3, command=lambda:functions_pack.number_pressed('.'))
        button_dot.grid(row=5, column=4)
        button_equals = Button(myFrame, text="=", pady=10, width=3, command=lambda:functions_pack.the_result())
        button_equals.grid(row=5, column=6)
        button_sum = Button(myFrame, text="+", pady=30, width=3, command=lambda:functions_pack.addition(functions_pack.screen_number.get()))
        button_sum.grid(row=4, column=5, rowspan=2)

        root.mainloop()
