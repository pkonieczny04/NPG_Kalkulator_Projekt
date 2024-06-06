import tkinter as tk
from tkinter import messagebox

class CalculatorGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")
        self.expression = ""
        self.entry = tk.Entry(root, width=40, borderwidth=5)
        self.entry.grid(row=0, column=0, columnspan=4)


    def create_buttons(self):
        button_texts = [
            "7", "8", "9", "/", "4", "5", "6", "*", 
            "1", "2", "3", "-", "0", ".", "=", "+", 
            "(", ")", "sqrt", "clear", "^", "i"
        ]
        row = 1
        col = 0
        for text in button_texts:
            button = tk.Button(self.root, text=text, padx=20, pady=20,
                               command=lambda t=text: self.on_button_click(t))
            button.grid(row=row, column=col)
            col += 1
            if col == 4:
                col = 0
                row += 1
