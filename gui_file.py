import tkinter as tk
from tkinter import messagebox

class CalculatorGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")
        self.expression = ""
        self.entry = tk.Entry(root, width=40, borderwidth=5)
        self.entry.grid(row=0, column=0, columnspan=4)
