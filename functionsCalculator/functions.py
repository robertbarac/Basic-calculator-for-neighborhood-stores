from tkinter import StringVar

class Functions():

    def __init__(self):
        self.operation:str = ""
        self.result = 0
        self.screenNumber = StringVar()
        self.screenNumber.set("0")

    #----------------------------key pressed method-----------
    def number_pressed(self, num: str):
        #Initial case: 0 in screen, numeric key pressed is 0 or 00
        if (num == "0" and self.screenNumber.get() == "0") or (num == "00" and self.screenNumber.get() == "0"):
            pass

        #Initial case: 0 in screen, numeric key pressed different of 0 and 00
        elif self.screenNumber.get() == "0":
            self.screenNumber.set(num)

        #There is a number different of 0 in screen
        elif self.screenNumber.get() != "0":
            self.screenNumber.set(self.screenNumber.get() + num)
        
        #Reset the number in screen if any numeric key is pressed and if there is a mathematic operation in process
        if self.operation != "":
            self.screenNumber.set(num)
            if self.result == 0:
                self.operation = ""

    #-----------------------addition method-----------------------
    def addition(self, num):
        # if self.result != 0:
        #     self.acumulated_result(num)
        # else:
        #     if self.screen_number_is_int():
        #         self.result += float(self.screenNumber.get())
        #     else:
        #         self.result += int(self.screenNumber.get())
        # self.operation = "addition"
        pass

    #-----------------------sustraction method-----------------
    def subtraction(self, num):
        # if self.result != 0:
        #     self.acumulated_result(num)
        # else:
        #     if self.screen_number_is_int():
        #         self.result += float(self.screenNumber.get())
        #     else:
        #         self.result += int(self.screenNumber.get())
        # self.operation = "subtraction"
        pass

    #-----------------------multiplication method--------------
    def multiplication(self, num):
        # if self.result != 0:
        #     self.acumulated_result(num)
        # else:
        #     if self.screen_number_is_int():
        #         self.result += float(self.screenNumber.get())
        #     else:
        #         self.result += int(self.screenNumber.get())
        # self.operation = "multiplication"
        pass

    #-----------------------division method--------------------
    def division(self, num):
        # if self.result != 0:
        #     self.acumulated_result(num)
        # else:
        #     if self.screen_number_is_int():
        #         self.result += float(self.screenNumber.get())
        #     else:
        #         self.result += int(self.screenNumber.get())
        # self.operation = "division"
        pass
    #----------------------result acumulated method-------------
    def acumulated_result(self, num):
        # if self.operation == "addition":
        #     if self.is_int():
        #         self.result += int(num)
        #     else:
        #         self.result += float(num)
        # elif self.operation == "subtraction":
        #     self.result -= int(num)
        #     #self.screenNumber.get()
        # elif self.operation == "multiplication":
        #     self.result *= float(num)
        # elif self.operation == "division":
        #     self.result /= float(num)
        pass

    #----------------------the_result method------------------
    def the_result(self):
        # if self.operation == "addition":
        #     self.result += float(self.screenNumber.get())
        #     if len(str(self.result)[str(self.result).find('.'):len(str(self.result)) + 1]) == 2 and (str(self.result)[str(self.result).find('.') + 1] == '0'):
        #         self.screenNumber.set(round(self.result))
        #     else:
        #         self.screenNumber.set(self.result)
            
        # elif self.operation == "subtraction":
        #     self.result -= float(self.screenNumber.get())
        #     if len(str(self.result)[str(self.result).find('.'):len(str(self.result)) + 1]) == 2 and (str(self.result)[str(self.result).find('.') + 1] == '0'):
        #         self.screenNumber.set(round(self.result))
        #     else:
        #         self.screenNumber.set(self.result)
        # elif self.operation == "multiplication":
        #     self.result = self.result * float(self.result * float(self.screenNumber.get()))
        #     if len(str(self.result)[str(self.result).find('.'):len(str(self.result)) + 1]) == 2 and (str(self.result)[str(self.result).find('.') + 1] == '0'):
        #         self.screenNumber.set(round(self.result))
        #     else:
        #         self.screenNumber.set(self.result)
            
        # elif self.operation == "division":
        #     self.result /= float(self.screenNumber.get())
        #     if len(str(self.result)[str(self.result).find('.'):len(str(self.result)) + 1]) == 2 and (str(self.result)[str(self.result).find('.') + 1] == '0'):
        #         self.screenNumber.set(round(self.result))
        #     else:
        #         self.screenNumber.set(self.result)
        # #self.result = 0
        # self.operation = ''
        pass

    def result_is_int(self):
        # return True if type(self.result) == 'int' else False
        pass

    def screen_number_is_int(self):
        # return True if '.' in str(self.screenNumber.get()) else False
        pass

    def clear_screen(self):
        self.screenNumber.set('0')
        #pass

    def clear_all(self):
        # self.screenNumber.set('0')
        # self.result = 0
        # self.operation = ''
        pass