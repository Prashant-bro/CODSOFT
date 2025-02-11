import random as rd  
import tkinter as tk 


win=tk.Tk()
win.geometry("400x400")
win.title("Password generator")
win.configure(bg="sky blue")

#info
l2=tk.Label(text="Enter Password Length:",font=("Arial",20))
l2.pack(pady=5)
#1 entry
e1=tk.Entry(font=("Arial",20))
e1.pack(pady=20)
# 1 label
l1=tk.Label(text="Password",font=("Arial",20))
l1.pack(pady=35)

#logic
def ans():
    str1="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()"
    pass1=""
    for i in range(int(e1.get())):
        pass1+=rd.choice(str1)
    l1.config(text=pass1)
    print("X")

#button
b1=tk.Button(text="Generate",font=("Arial",20),command=ans)
b1.pack(pady=15)
win.mainloop()