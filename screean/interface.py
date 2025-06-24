import tkinter as tk
from tkinter import messagebox

class App:
    def __init__(self, master):
        self.master = master
        self.master.title("Register")
        self.master.geometry("400x300")

        # Frame main
        self.frame = tk.Frame(master)
        self.frame.pack(expand=True)
        
        tk.Label(self.frame, text="cadastro").grid(row=0, column=1, padx=20, pady=20, sticky="nw")
        
        tk.Label(self.frame, text="Glass").grid(row=1, column=0, padx=10, pady=10, sticky="nw")
        self.entry_glass = tk.Entry(self.frame).grid(row=1, column=1)
        
        tk.Label(self.frame, text="Color").grid(row=2, column=0, padx=10, pady=10, sticky="nw")
        self.entry_color = tk.Entry(self.frame).grid(row=2, column=1)
        
        tk.Label(self.frame, text="Box").grid(row=3, column=0, padx=10, pady=10, sticky="nw")
        self.entry_box = tk.Entry(self.frame).grid(row=3, column=1)
        
        tk.Label(self.frame, text="Multiplied").grid(row=4, column=0, padx=10, pady=10, sticky="nw")
        self.entry_multiplied = tk.Entry(self.frame).grid(row=4, column=1)
        
        self.button = tk.Button(self.frame, text="Send").grid(row=5, column=1, padx=15, pady=15)
        
    
     

# Inicializa a janela principal
if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
