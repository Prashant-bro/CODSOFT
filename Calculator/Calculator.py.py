import tkinter as tk 

win=tk.Tk()
win.geometry("400x400")
win.title("Calculator")
win.configure(bg="sky blue")


# for_info
l2=tk.Label(text="NO-1",font=("Arial",20))
l2.pack()
# Entry
e1=tk.Entry(font=("Arial",20))
e1.pack(pady=10)

# for_info
l2=tk.Label(text="NO-2",font=("Arial",20))
l2.pack()

#2nd Entry
e2=tk.Entry(font=("Arial",20))
e2.pack(pady=25)

# Label
l1=tk.Label(text="RESULT",font=("Arial",20))
l1.pack(pady=20)


# Button
def add():
    a=int(e1.get())
    b=int(e2.get())
    c=a+b
    l1.config(text=c)
def sub():
    a=int(e1.get())
    b=int(e2.get())
    c=a-b
    l1.config(text=c)
def multi():
    a=int(e1.get())
    b=int(e2.get())
    c=a*b
    l1.config(text=c)
def divi():
    a=int(e1.get())
    b=int(e2.get())
    c=a/b
    l1.config(text=c)

b1=tk.Button(text="ADD",font=("Arial",20),command=add)
b1.pack(pady=10)

b2=tk.Button(text="SUB",font=("Arial",20),command=sub)
b2.pack(pady=10)

b3=tk.Button(text="MULTI",font=("Arial",20),command=multi)
b3.pack(pady=10)

b4=tk.Button(text="DIV",font=("Arial",20),command=divi)
b4.pack(pady=10)
    
win.mainloop()