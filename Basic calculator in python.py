import tkinter as tk

class Calculator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Calculator")
        self.expression = tk.StringVar()

        entry = tk.Entry(self, textvariable=self.expression, font=("Arial", 16))
        entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

        buttons = [
            ("1", 1, 0), ("2", 1, 1), ("3", 1, 2), ("/", 1, 3),
            ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
            ("7", 3, 0), ("8", 3, 1), ("9", 3, 2), ("-", 3, 3),
            ("0", 4, 0), (".", 4, 1), ("+", 4, 3), ("%", 5, 3)
        ]

        for (text, row, col) in buttons:
            btn = tk.Button(self, text=text, width=5, height=2, font=("Arial", 12), command=lambda t=text: self.on_button_click(t))
            btn.grid(row=row, column=col, padx=5, pady=5)

        clear_btn = tk.Button(self, text="C", width=11, height=2, font=("Arial", 12), command=self.clear)
        clear_btn.grid(row=6, column=0, columnspan=2, padx=5, pady=5)

        equal_btn = tk.Button(self, text="=", width=11, height=2, font=("Arial", 12), command=self.calculate)
        equal_btn.grid(row=6, column=2, columnspan=2, padx=5, pady=5)

    def on_button_click(self, text):
        current_expression = self.expression.get()
        if text == "C":
            self.clear()
        elif text == "=":
            self.calculate()
        else:
            self.expression.set(current_expression + text)

    def clear(self):
        self.expression.set("")

    def calculate(self):
        try:
            result = eval(self.expression.get())
            self.expression.set(str(result))
        except:
            self.expression.set("Error")

if __name__ == "__main__":
    app = Calculator()
    app.mainloop()
