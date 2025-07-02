import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

#interface import
from add_product import Add_product
from remove_product import Remove_product
  
  
  
  
class App:
    def __init__(self, master):
        self.master = master
        self.master.title("Register")
        self.master.geometry("300x250")    
        
        
        #creating tabs
        self.notebook = ttk.Notebook(master)
        self.notebook.pack(expand=True,  fill="both")
       
        self.frame =Add_product (self.notebook)
        self.frame2 =Remove_product(self.notebook)
        
         
        self.notebook.add(self.frame, text="Register")
        self.notebook.add(self.frame2, text="Remove")
        

            
#star windows main
if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
