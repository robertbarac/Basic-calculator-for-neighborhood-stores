# from setButtonsCalculator import screenNumber, result
from tkinter import StringVar

class Functions():

    def __init__(self):
        self.operation:str = ""
        self.result = 0
        self.screenNumber = StringVar()

    #----------------------------key pressed method-----------
    def number_pressed(self, num: str):
        if self.operation != "":
            self.screenNumber.set(num)
            if self.result == 0:
                self.operation = ""
        else:
            self.screenNumber.set(self.screenNumber.get() + num)

    #-----------------------addition method-----------------------
    def addition(self, num):
        if self.result != 0:
            self.acumulated_result(num)
        else:
            if type(self.result) == 'int':
                self.result += int(num)
            else:
                self.result += float(num)
        self.operation = "addition"
        self.screenNumber.set(self.result)

    #-----------------------sustraction method-----------------
    def subtraction(self, num):
        if self.result != 0:
            self.acumulated_result(num)
        else:
            self.result += int(num)
        self.operation = "subtraction"
        self.screenNumber.set(self.result)

    #-----------------------multiplication method--------------
    def multiplication(self, num):
        if self.result != 0:
            self.acumulated_result(num)
        else:
            self.result += int(num)
        self.operation = "multiplication"
        self.screenNumber.set(self.result)

    #-----------------------division method--------------------
    def division(self, num):
        if self.result != 0:
            self.acumulated_result(num)
        else:
            self.result += int(num)
        self.operation = "division"
        self.screenNumber.set(self.result)
    
    #----------------------result acumulated method-------------
    def acumulated_result(self, num):
        if self.operation == "addition":
            if self.is_int():
                self.result += int(num)
            else:
                self.result += float(num)
        elif self.operation == "subtraction":
            self.result -= int(num)
            #self.screenNumber.get()
        elif self.operation == "multiplication":
            self.result *= int(num)
        elif self.operation == "division":
            self.result /= int(num)

    #----------------------the_result method------------------
    def the_result(self):
        if self.operation == "addition":
            self.screenNumber.set(self.result + int(self.screenNumber.get()))
        elif self.operation == "subtraction":
            self.screenNumber.set(self.result - int(self.screenNumber.get()))
        elif self.operation == "multiplication":
            self.screenNumber.set(self.result * int(self.screenNumber.get()))
        elif self.operation == "division":
            if self.result % int(self.screenNumber.get()) == 0:
                self.screenNumber.set(int(self.result / int(self.screenNumber.get())))
            else:
                self.screenNumber.set(self.result / int(self.screenNumber.get()))
        self.result = 0

    def is_int(self):
        return True if type(self.result) == 'int' else 'float'
