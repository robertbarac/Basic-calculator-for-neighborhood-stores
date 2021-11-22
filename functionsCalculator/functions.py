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
        elif num == '.' and self.screenNumber.get() == '0':
            self.screenNumber.set(self.screenNumber.get + num)
        #there is in the screen a number diferent to zero
        elif num == '.' and self.screenNumber.get() != '0':
            #there is a dot in the screen
            if '.' in self.screenNumber.get():
                pass
            #there is no a dot in the screen, add the dot in the screen
            else:
                self.screenNumber.set(self.screenNumber.get() + num)
        elif self.screenNumber.get() == "":
            self.screenNumber.set(num)
        #Initial case: 0 in screen, numeric key pressed different of 0 and 00
        elif self.screenNumber.get() == "0" and self.result == 0:
            self.screenNumber.set(num)

        #There is a number different of 0 in screen
        elif self.screenNumber.get() != "0" and self.result == 0:
            self.screenNumber.set(self.screenNumber.get() + num)

        #Reset the number in screen if any numeric key is pressed and if there is a mathematic operation in process
        elif self.operation != "":
            if self.screenNumber.get() == "0":
                self.screenNumber.set(num)
            elif self.flag_result == self.flag_screen:
                self.screenNumber.set(num)
                self.flag_screen = False
            elif self.flag_result != self.flag_screen:
                self.screenNumber.set(self.screenNumber.get() + num)
            if self.result == 0:
                self.operation = ""
                self.flag_result = False
    
    def selector(self, operation:str):
        self.flag_screen = True
        if self.operation == '':
            if self.result == 0:
                self.result += float(self.screenNumber.get())
            self.operation == operation
        elif self.operation == 'addition':
            self.result += float(self.screenNumber.get())
        elif self. operation == 'subtraction':
            self.result -= float(self.screenNumber.get())
        elif self. operation == 'multiplication':
            self.result *= float(self.screenNumber.get())
        elif self. operation == 'division':
            self.result /= float(self.screenNumber.get())
        if len(str(self.result)[str(self.result).find('.'):len(str(self.result)) + 1]) == 2 and (str(self.result)[str(self.result).find('.') + 1] == '0'):
            self.result = int(self.result)
            self.screenNumber.set(self.result)
            self.flag_result = True
        else:
            self.screenNumber.set(self.result)
            self.flag_result = True
        self.operation = operation

    #-----------------------addition method-----------------------
    def addition(self, num:str):
        self.selector('addition')

    #-----------------------sustraction method-----------------
    def subtraction(self, num):
        self.selector('subtraction')


    #-----------------------multiplication method--------------
    def multiplication(self, num):
        self.selector('multiplication')

    #-----------------------division method--------------------
    def division(self, num):
        self.selector('division')


    def print_in_screen(self):
        if len(str(self.result)[str(self.result).find('.'):len(str(self.result)) + 1]) == 2 and (str(self.result)[str(self.result).find('.') + 1] == '0'):
            self.screenNumber.set(round(self.result))
            self.flag_result = True
        else:
            self.screenNumber.set(self.result)
            self.flag_result = True

    #----------------------the_result method------------------
    def the_result(self):
        if self.result == 0:
            pass
        elif self.operation == "":
            self.result += float(self.screenNumber.get())
            self.screenNumber.set(self.result)
        elif self.operation == "addition":
            self.result += float(self.screenNumber.get())
            self.print_in_screen()
            
        elif self.operation == "subtraction":
            self.result -= float(self.screenNumber.get())
            self.print_in_screen()
        elif self.operation == "multiplication":
            self.result = self.result * float(self.screenNumber.get())
            self.print_in_screen()
            
        elif self.operation == "division":
            self.result /= float(self.screenNumber.get())
            self.print_in_screen()
        self.operation = ''
    
    def square_root(self):
        if int(self.screenNumber.get()) == 0:
            self.screenNumber.set('0')
        else:
            self.sqrt = float(self.screenNumber.get() ** (0.5))
            self.result = self.sqrt
            self.print_in_screen()

    def percentage(self):
        if self.screenNumber.get() == '0':
            self.screenNumber.set('0')
        else:
            self.prctg = self.result * (float(self.screenNumber.get()) / 100)
            self.result = self.prctg
            self.print_in_screen()


    def result_is_int(self):
        return True if type(self.result) == 'int' else False

    def screen_number_is_int(self):
        return False if '.' in str(self.screenNumber.get()) else True

    def delete_last_number(self):
        self.old_number:str = self.screenNumber.get()
        self.new_number:str = self.old_number[:-1]
        self.screenNumber.set(self.new_number)

    def negative_or_positive_number(self):
        self.string:str = self.screenNumber.get()
        if self.string[0] == '-':
            self.screenNumber.set(self.string[1:])
        else:
            self.screenNumber.set('-' + self.string)

    def clear_screen(self):
        self.screenNumber.set('')

    def clear_all(self):
        self.screenNumber.set('0')
        self.result = 0
        self.operation = ''
        self.flag_result = False
        self.flag_screen = False