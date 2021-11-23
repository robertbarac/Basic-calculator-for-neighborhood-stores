from tkinter import StringVar

class Functions():

    def __init__(self):
        self.operation: str = ""
        self.result = 0
        self.screen_number = StringVar()
        self.screen_number.set("0")
        self.flag_result = False
        self.flag_screen = False

    # ----------------------------key pressed method-----------
    def number_pressed(self, num: str):
        # Initial case: 0 in screen, numeric key pressed is 0 or 00
        if (num == "0" and self.screen_number.get() == "0") or (num == "00" and self.screen_number.get() == "0"):
            pass
        elif num == '.' and self.screen_number.get() == '0':
            self.screen_number.set(self.screen_number.get + num)
        # there is in the screen a number different to zero
        elif num == '.' and self.screen_number.get() != '0':
            # there is a dot in the screen
            if '.' in self.screen_number.get():
                pass
            # there is no a dot in the screen, add the dot in the screen
            else:
                self.screen_number.set(self.screen_number.get() + num)
        elif self.screen_number.get() == "":
            self.screen_number.set(num)
        # Initial case: 0 in screen, numeric key pressed different of 0 and 00
        elif self.screen_number.get() == "0" and self.result == 0:
            self.screen_number.set(num)

        # There is a number different of 0 in screen
        elif self.screen_number.get() != "0" and self.result == 0:
            self.screen_number.set(self.screen_number.get() + num)

        # Reset the number in screen if any numeric key is pressed and if there is a mathematic operation in process
        elif self.operation != "":
            if self.screen_number.get() == "0":
                self.screen_number.set(num)
            elif self.flag_result == self.flag_screen:
                self.screen_number.set(num)
                self.flag_screen = False
            elif self.flag_result != self.flag_screen:
                self.screen_number.set(self.screen_number.get() + num)
            if self.result == 0:
                self.operation = ""
                self.flag_result = False
    
    def selector(self, operacion: str):
        self.flag_screen = True
        if self.operation == '':
            if self.result == 0:
                self.result += float(self.screen_number.get())
            self.operation == operacion
        elif self.operation == 'addition':
            self.result += float(self.screen_number.get())
        elif self. operation == 'subtraction':
            self.result -= float(self.screen_number.get())
        elif self. operation == 'multiplication':
            self.result *= float(self.screen_number.get())
        elif self. operation == 'division':
            self.result /= float(self.screen_number.get())
        if len(str(self.result)[str(self.result).find('.'):len(str(self.result)) + 1]) == 2 and (str(self.result)[str(self.result).find('.') + 1] == '0'):
            self.result = int(self.result)
            self.screen_number.set(self.result)
            self.flag_result = True
        else:
            self.screen_number.set(self.result)
            self.flag_result = True
        self.operation = operacion

    # -----------------------addition method-----------------------
    def addition(self, num: str):
        self.selector('addition')

    # subtraction method
    def subtraction(self, num):
        self.selector('subtraction')


    # multiplication method
    def multiplication(self, num):
        self.selector('multiplication')

    # -----------------------division method--------------------
    def division(self, num):
        self.selector('division')


    def print_in_screen(self):
        if len(str(self.result)[str(self.result).find('.'):len(str(self.result)) + 1]) == 2 and (str(self.result)[str(self.result).find('.') + 1] == '0'):
            self.screen_number.set(round(self.result))
            self.flag_result = True
        else:
            self.screen_number.set(self.result)
            self.flag_result = True

    # ----------------------the_result method------------------
    def the_result(self):
        if self.result == 0:
            pass
        elif self.operation == "":
            self.result += float(self.screen_number.get())
            self.screen_number.set(self.result)
        elif self.operation == "addition":
            self.result += float(self.screen_number.get())
            self.print_in_screen()
            
        elif self.operation == "subtraction":
            self.result -= float(self.screen_number.get())
            self.print_in_screen()
        elif self.operation == "multiplication":
            self.result = self.result * float(self.screen_number.get())
            self.print_in_screen()
            
        elif self.operation == "division":
            self.result /= float(self.screen_number.get())
            self.print_in_screen()
        self.operation = ''
    
    def square_root(self):
        if int(self.screen_number.get()) == 0:
            self.screen_number.set('0')
        else:
            self.sqrt = float(self.screen_number.get()) ** (0.5)
            self.result = self.sqrt
            self.print_in_screen()

    def percentage(self):
        if self.screen_number.get() == '0':
            self.screen_number.set('0')
        elif self.screen_number.get() != '0':
            if self.result == 0:
                self.prctg = (float(self.screen_number.get()) / 100)
            else:
                self.prctg = self.result * (float(self.screen_number.get()) / 100)
            self.result = self.prctg
            self.print_in_screen()


    def result_is_int(self):
        return True if type(self.result) == 'int' else False

    def _is_int(self):
        return False if '.' in str(self.screen_number.get()) else True

    def delete_last_number(self):
        self.old_number:str = self.screen_number.get()
        self.new_number:str = self.old_number[:-1]
        self.screen_number.set(self.new_number)

    def negative_or_positive_number(self):
        self.string:str = self.screen_number.get()
        if self.string[0] == '-':
            self.screen_number.set(self.string[1:])
        else:
            self.screen_number.set('-' + self.string)

    def clear_screen(self):
        self.screen_number.set('')

    def clear_all(self):
        self.screen_number.set('0')
        self.result = 0
        self.operation = ''
        self.flag_result = False
        self.flag_screen = False