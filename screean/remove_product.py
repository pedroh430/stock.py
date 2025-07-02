import tkinter as tk
import sqlite3 



class Remove_product (tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.pack_propagate(True)
        
        self.remove_glass = tk.StringVar()
        self.color = tk.StringVar()
        self.box = tk.IntVar()
        self.unit = tk.IntVar()
        
        
        
        def remove():
             conn = sqlite3.connect("database")
             cur = conn.cursor()
             valor = self.remove_glass.get()
             
             cur.execute("DELETE FROM stock WHERE type =?", (valor))
             
             conn.commit()
             conn.close()
             
             
            
        
         
        tk.Label(self, text="Remove").grid(row=0, column=1, padx=20, pady=20, sticky="nswe")
        
        tk.Label(self, text="Glass").grid(row=1, column=0, padx=10, pady=10, sticky="nswe")
        self.entry_glass = tk.Entry(self, textvariable= self.remove_glass).grid(row=1, column=1)
        
        tk.Label(self, text="Color").grid(row=2, column=0, padx=10, pady=10, sticky="nswe")
        self.entry_color = tk.Entry(self).grid(row=2, column=1)
        
        tk.Label(self, text="Box").grid(row=3, column=0, padx=10, pady=10, sticky="nswe")
        self.entry_box = tk.Entry(self).grid(row=3, column=1)
        
        tk.Label(self, text="Multiplied").grid(row=4, column=0, padx=10, pady=10, sticky="nswe")
        self.entry_multiplied = tk.Entry(self).grid(row=4, column=1)
        
        self.button = tk.Button(self, text="Send", command=remove).grid(row=5, column=1, padx=15, pady=15)
        