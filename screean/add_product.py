import tkinter as tk
from tkinter import ttk
import sqlite3 

            



        

class Add_product(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.pack_propagate(False)
        
    
        #variables
        self.glass = tk.StringVar()
        self.color = tk.StringVar()
        self.box = tk.IntVar()
        self.unit = tk.IntVar()
       
        def end(self):
            conn = sqlite3.connect()
            cursor = conn.cursor()
            
            
            conn.close()
            
            
        
            
           
            
         
         
        tk.Label(self, text="cadastro").grid(row=0, column=1, padx=20, pady=20, sticky="nswe")
        
        tk.Label(self, text="Glass").grid(row=1, column=0, padx=10, pady=10, sticky="nswe")
        self.entry_glass = tk.Entry(self, textvariable=self.glass).grid(row=1, column=1)
        
        tk.Label(self, text="Color").grid(row=2, column=0, padx=10, pady=10, sticky="nswe")
        self.entry_color = tk.Entry(self, textvariable=self.color).grid(row=2, column=1)
        
        tk.Label(self, text="Box").grid(row=3, column=0, padx=10, pady=10, sticky="nswe")
        self.entry_box = tk.Entry (self, textvariable= self.box).grid(row=3, column=1)
        
        tk.Label(self, text="Multiplied").grid(row=4, column=0, padx=10, pady=10, sticky="nswe")
        self.entry_multiplied = tk.Entry(self, textvariable= self.unit).grid(row=4, column=1)
        
        self.button = tk.Button(self, text="Send", command= ola).grid(row=5, column=1, padx=15, pady=15)
        
        
   
        
        
        