from tkinter import StringVar

class Functions():

    def __init__(self):
        self.operation:str = ""
        self.result = 0
        self.screenNumber = StringVar()
        self.screenNumber.set("0")
        self.flag_result = False
        self.flag_screen = False

    #----------------------------key pressed method-----------
    def number_pressed(self, num: str):
        #Initial case: 0 in screen, numeric key pressed is 0 or 00
        if (num == "0" and self.screenNumber.get() == "0") or (num == "00" and self.screenNumber.get() == "0"):
            pass
        elif self.screenNumber.get() == "":
            self.screenNumber.set(num)
        #Initial case: 0 in screen, numeric key pressed different of 0 and 00
        elif self.screenNumber.get() == "0" and self.result == 0:
            self.screenNumber.set(num)

        #There is a number different of 0 in screen
        elif self.screenNumber.get() != "0" and self.result == 0:
            print("por aquí")
            self.screenNumber.set(self.screenNumber.get() + num)
        
        #Reset the number in screen if any numeric key is pressed and if there is a mathematic operation in process
        elif self.operation != "":
            if self.screenNumber.get() == "0":
                self.screenNumber.set(num)
            elif self.flag_result == self.flag_screen:
                self.screenNumber.set(num)
                self.flag_screen = False
            elif self.flag_result != self.flag_screen:
                print("por acá")
                print(self.result)
                self.screenNumber.set(self.screenNumber.get() + num)
            if self.result == 0:
                self.operation = ""
                self.flag_result = False

    #-----------------------addition method-----------------------
    def addition(self, num:str):
        self.flag_screen = True
        self.operation = "addition"
        if self.result != 0:
            self.acumulated_result(num)
        else:
            if self.screen_number_is_int():
                self.result += float(self.screenNumber.get())
                self.flag_result = True
            else:
                self.result += int(self.screenNumber.get())
                self.flag_result = True
        #pass

    #-----------------------sustraction method-----------------
    def subtraction(self, num):
        # self.operation = "subtraction"
        # if self.result != 0:
        #     self.acumulated_result(num)
        # else:
        #     if self.screen_number_is_int():
        #         self.result += int(self.screenNumber.get())
        #     else:
        #         self.result += float(self.screenNumber.get())
        pass

    #-----------------------multiplication method--------------
    def multiplication(self, num):
        # self.operation = "multiplication"
        # if self.result != 0:
        #     self.acumulated_result(num)
        # else:
        #     if self.screen_number_is_int():
        #         self.result += float(self.screenNumber.get())
        #     else:
        #         self.result += int(self.screenNumber.get())
        pass

    #-----------------------division method--------------------
    def division(self, num):
        # self.operation = "division"
        # if self.result != 0:
        #     self.acumulated_result(num)
        # else:
        #     if self.screen_number_is_int():
        #         self.result += float(self.screenNumber.get())
        #     else:
        #         self.result += int(self.screenNumber.get())
        pass
    #----------------------result acumulated method-------------
    def acumulated_result(self, num):
        if self.operation == "addition":
            if self.result_is_int():
                self.result += int(num)
                self.flag_result = True
            else:
                self.result += float(num)
                self.flag_result = True
        # elif self.operation == "subtraction":
        #     self.result -= int(num)
        #     #self.screenNumber.get()
        # elif self.operation == "multiplication":
        #     self.result *= float(num)
        # elif self.operation == "division":
        #     self.result /= float(num)
        #pass

    #----------------------the_result method------------------
    def the_result(self):
        if self.result == 0:
            pass
        if self.operation == "addition":
            self.result += float(self.screenNumber.get())
            if len(str(self.result)[str(self.result).find('.'):len(str(self.result)) + 1]) == 2 and (str(self.result)[str(self.result).find('.') + 1] == '0'):
                self.screenNumber.set(round(self.result))
                self.flag_result = True
            else:
                self.screenNumber.set(self.result)
                self.flag_result = True
            
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
        self.result = 0
        #self.operation = ''
        pass

    def result_is_int(self):
        return True if type(self.result) == 'int' else False

    def screen_number_is_int(self):
        return False if '.' in str(self.screenNumber.get()) else True

    def delete_last_number(self):
        pass

    def clear_screen(self):
        self.screenNumber.set('')
        #pass

    def clear_all(self):
        self.screenNumber.set('0')
        self.result = 0
        self.operation = ''
        self.flag_result = False
        self.flag_screen = False
        #pass