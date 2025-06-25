import tkinter as tk


class Romeve_product(tk.Frame):
   def __init__(self, parent):
       super().__init__(parent)
       self.pack_propagate(False)
       
       tk.Label(self, text="Remove").grid(row=0, column=1, padx=20, pady=20, sticky="nswe")
       
       
       tk.Label(self, text="Color").grid(row=1, column=0, padx=10, pady=10, sticky="nswe" )
       self.remove_color = tk.Entry(self).grid(row=1, column=1, padx=10, pady=10, sticky="nwse")