import tkinter as tk
from tkinter import messagebox
from calculator import Calculator

class CalculatorGUI:
    def __init__(self, root):
        self.calc = Calculator()
        self.root = root
        self.root.title("Calculator")

        self.expression = ""
        self.entry = tk.Entry(root, width=40, borderwidth=5)
        self.entry.grid(row=0, column=0, columnspan=4)

        self.create_buttons()

    def create_buttons(self):
        button_texts = [
            "7", "8", "9", "/",
            "4", "5", "6", "*",
            "1", "2", "3", "-",
            "0", ".", "=", "+",
            "(", ")", "sqrt", "clear",
            "^", "i", "History"
        ]

        row = 1
        col = 0

        for text in button_texts:
            button = tk.Button(self.root, text=text, padx=20, pady=20, command=lambda t=text: self.on_button_click(t))
            button.grid(row=row, column=col)
            col += 1
            if col == 4:
                col = 0
                row += 1

    def on_button_click(self, char):
        if char == "=":
            self.evaluate_expression()
        elif char == "clear":
            self.expression = ""
            self.entry.delete(0, tk.END)
        elif char == "sqrt":
            self.expression += "sqrt("
            self.entry.insert(tk.END, "sqrt(")
        elif char == "History":
            self.show_history()
        else:
            self.expression += str(char)
            self.entry.insert(tk.END, char)

    def evaluate_expression(self):
        try:
            # Przygotowanie wyrażenia do obliczenia
            expression = self.expression
            result = self.calc.evaluate_expression(expression)
            display_result = str(result)
            self.entry.delete(0, tk.END)
            self.entry.insert(tk.END, display_result)
            self.expression = ""
        except Exception as e:
            messagebox.showerror("Error", str(e))
            self.expression = ""
            self.entry.delete(0, tk.END)

    def show_history(self):
        history_window = tk.Toplevel(self.root)
        history_window.title("History")
        history_text = tk.Text(history_window, wrap=tk.WORD)
        history_text.pack(expand=True, fill=tk.BOTH)
        
        for index, operation in enumerate(self.calc.history, start=1):
            history_text.insert(tk.END, f"{index}. {operation}\n")
        history_text.config(state=tk.DISABLED)

if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorGUI(root)
    root.mainloop()