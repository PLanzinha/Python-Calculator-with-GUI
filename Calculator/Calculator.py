import tkinter as tk

LARGE_FONT_STYLE = ("Arial", 28, "bold")
SMALL_FONT_STYLE = ("Arial", 10)
DIGIT_FONT_STYLE = ("Arial", 24, "bold")
DEFAULT_FONT_STYLE = ("Arial", 20)

OFF_WHITE = "#F8FAFF"
WHITE = "#FFFFFF"
LIGHT_GRAY = "#F5F5F5"
LABEL_COLOR = "#25265E"
LIGHT_BLUE = "#CCEDFF"


class Calculator:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Calculator")
        self.window.geometry("350x600")
        self.window.resizable(True, True)

        self.memory_display = ""
        self.total_display = ""

        self.display_frame = self.create_display_frame()
        self.memory_label, self.total_label = self.create_display_label()

        self.digits = {
            7: (1, 1), 8: (1, 2), 9: (1, 3),
            4: (2, 1), 5: (2, 2), 6: (2, 3),
            1: (3, 1), 2: (3, 2), 3: (3, 3),
            0: (4, 2), ',': (4, 3)
        }

        self.operators = {"/": "\u00F7", "*": "\u00D7", "-": "-", "+": "+", "=": "="}
        self.buttons_frame = self.create_buttons_frame()

        self.buttons_frame.rowconfigure(0, weight=1)
        for x in range(1, 5):
            self.buttons_frame.rowconfigure(x, weight=1)
            self.buttons_frame.columnconfigure(x, weight=1)

        self.create_digit_buttons()
        self.create_operator_buttons()
        self.create_special_function_buttons()

    def create_special_function_buttons(self):
        self.create_all_clear_button()
        self.create_clear_button()
        self.create_square_button()
        self.create_squareroot_button()

        self.create_equals_button()
     #  self.create_mempage_button()

    def create_display_label(self):
        memory_label = tk.Label(self.display_frame, text=self.memory_display, anchor=tk.E,
                                bg=LIGHT_GRAY, fg=LABEL_COLOR, padx=24, font=SMALL_FONT_STYLE)
        memory_label.pack(expand=True, fill="both")

        total_label = tk.Label(self.display_frame, text=self.total_display, anchor=tk.E,
                               bg=LIGHT_GRAY, fg=LABEL_COLOR, padx=24, font=LARGE_FONT_STYLE)
        total_label.pack(expand=True, fill="both")

        return memory_label, total_label

    def create_display_frame(self):
        frame = tk.Frame(self.window, height=230, bg=LIGHT_GRAY)
        frame.pack(expand=True, fill="both")
        return frame

    def add_to_display(self, value):
        self.total_display += str(value)
        self.update_total_value()

    def create_digit_buttons(self):
        for digit, grid_value in self.digits.items():
            button = tk.Button(self.buttons_frame, text=str(digit),
                               bg=WHITE, fg=LABEL_COLOR, font=DIGIT_FONT_STYLE, borderwidth=0,
                               command=lambda x=digit: self.add_to_display(x))
            button.grid(row=grid_value[0], column=grid_value[1], sticky=tk.NSEW)

    def append_operator(self, operator):
        self.total_display += operator
        self.memory_display = self.total_display
        self.update_memory_value()
        self.update_total_value()

    def create_operator_buttons(self):
        i = 0
        for operator, symbol in self.operators.items():
            button = tk.Button(self.buttons_frame, text=symbol,
                               bg=OFF_WHITE, fg=LABEL_COLOR, font=DEFAULT_FONT_STYLE, borderwidth=0,
                               command=lambda x=operator: self.append_operator(x))
            button.grid(row=i, column=4, sticky=tk.NSEW)
            i += 1

    def all_clear(self):
        self.total_display = ""
        self.memory_display = ""
        self.update_memory_value()
        self.update_total_value()

    def create_all_clear_button(self):
        for operator, symbol in self.operators.items():
            button = tk.Button(self.buttons_frame, text="CA",
                               bg=OFF_WHITE, fg=LABEL_COLOR, font=DEFAULT_FONT_STYLE, borderwidth=0,
                               command=self.all_clear)
            button.grid(row=0, column=1, sticky=tk.NSEW, columnspan=1)

    def clear(self):
        self.total_display = self.total_display[:-1]
        self.update_total_value()

    def create_clear_button(self):
        for operator, symbol in self.operators.items():
            button = tk.Button(self.buttons_frame, text="C",
                               bg=OFF_WHITE, fg=LABEL_COLOR, font=DEFAULT_FONT_STYLE, borderwidth=0,
                               command=self.clear)
            button.grid(row=0, column=2, sticky=tk.NSEW, columnspan=1)

    def square(self):
        if self.total_display == "":
            self.total_display = ""
        else:
            self.total_display = str(eval(F"{self.total_display}**2"))  # f or F string
        self.memory_display = self.total_display
        self.update_total_value()
        self.update_memory_value()

    def create_square_button(self):
        for operator, symbol in self.operators.items():
            button = tk.Button(self.buttons_frame, text="x\u00b2",
                               bg=OFF_WHITE, fg=LABEL_COLOR, font=DEFAULT_FONT_STYLE, borderwidth=0,
                               command=self.square)
            button.grid(row=0, column=3, sticky=tk.NSEW, columnspan=1)

    def squareroot(self):
        if self.total_display == "":
            self.total_display = ""
        else:
            self.total_display = str(eval(F"{self.total_display}**2"))  # f or F string
        self.memory_display = self.total_display
        self.update_total_value()
        self.update_memory_value()

    def create_squareroot_button(self):
        for operator, symbol in self.operators.items():
            button = tk.Button(self.buttons_frame, text="x\u221a",
                               bg=OFF_WHITE, fg=LABEL_COLOR, font=DEFAULT_FONT_STYLE, borderwidth=0,
                               command=self.squareroot)
            button.grid(row=4, column=1, sticky=tk.NSEW, columnspan=1)

    def evaluate(self):
        self.update_memory_value()
        self.memory_display = self.total_display
        if self.total_display == "":
            self.total_display = ""
        else:
            try:
                self.total_display = str(eval(self.total_display))
            except Exception as e:
                self.total_display = "Error"
            finally:
                self.update_total_value()

        if self.memory_display == self.total_display:
            self.total_display = ""
        self.update_total_value()

    def create_equals_button(self):
        for operator, symbol in self.operators.items():
            button = tk.Button(self.buttons_frame, text="=",
                               bg=LIGHT_BLUE, fg=LABEL_COLOR, font=DEFAULT_FONT_STYLE, borderwidth=0,
                               command=self.evaluate)
            button.grid(row=4, column=4, sticky=tk.NSEW, columnspan=1)

#    def create_mempage_button(self):
#       for operator, symbol in self.operators.items():
#            button = tk.Button(self.buttons_frame, text="M",
#                               bg=WHITE, fg=LABEL_COLOR, font=DEFAULT_FONT_STYLE, borderwidth=0)
#            button.grid(row=4, column=1, sticky=tk.NSEW, columnspan=1)

    def create_buttons_frame(self):
        frame = tk.Frame(self.window)
        frame.pack(expand=True, fill="both")
        return frame

    def update_memory_value(self):
        expression = self.total_display
        for operator, symbol in self.operators.items():
            expression = expression.replace(operator, f' {symbol} ')
        self.memory_label.config(text=expression[:15])

    def update_total_value(self):
        expression = self.total_display
        for operator, symbol in self.operators.items():
            expression = expression.replace(operator, f' {symbol} ')
        self.total_label.config(text=expression[:15])

    def run(self):
        self.window.mainloop()


if __name__ == "__main__":
    calc = Calculator()
    calc.run()
