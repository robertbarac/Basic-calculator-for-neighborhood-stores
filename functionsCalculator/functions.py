# from setButtonsCalculator import screenNumber, result
from tkinter import StringVar

class Functions():

    def __init__(self):
        self.operation:str = ""
        self.result = 0
        self.screenNumber = StringVar()

    #----------------------------pulsaciones teclado-----------

    def numeroPulsado(self, num: str):
        global operation

        if self.operation != "":
            self.screenNumber.set(num)
            operation = ""
        else:
            self.screenNumber.set(self.screenNumber.get() + num)
            
    #-----------------------función suma-----------------------
    def suma(self, num):
        # global operation
        # global result
        self.result += int(num)
        self.operation = "suma"
        self.screenNumber.set(self.result)

    #-------- sustraction method-----------
    def sustraction(self, num):
        self.result += int(num)
        self.operation = "sustraction"
        self.screenNumber.set(self.result)

    #------------Función el_resultado----------------------------
    def el_resultado(self):
        #global result
        if self.operation == "suma":
            self.screenNumber.set(self.result + int(self.screenNumber.get()))
        elif self.operation == "sustraction":
            self.screenNumber.set(self.result - int(self.screenNumber.get()))

        self.result = 0
