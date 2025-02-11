import tkinter as tk 
from tkinter import messagebox
import mysql.connector as m


db = m.connect(
    host="localhost",
    user="root",
    passwd="CODER",
    database="ToDoApp"
)
cur = db.cursor()

win = tk.Tk()
win.title("To-Do List")
win.geometry("500x500")
win.configure(bg="sky blue")

tk.Label(win, text="Enter the Task:-", font=("Arial", 20), bg="sky blue").pack(pady=20)
e1 = tk.Entry(font=("Arial", 20))
e1.pack(pady=20)

def add_1():
    p = e1.get()
    if p:
        cur.execute("INSERT INTO tasks (task, status) VALUES (%s, %s)", (p, "Pending"))  # Modified: Added "Pending" status
        db.commit()
        e1.delete(0, tk.END)
        show_tasks()
        messagebox.showinfo("ADD","ADDED SIR!")
    else:
        messagebox.showwarning("Warning", "Task cannot be empty!")

b1 = tk.Button(text="ADD", font=("Arial", 20), command=add_1)
b1.pack(pady=10)

def show_tasks():
    cur.execute("SELECT id, task, status FROM tasks")  
    val_1 = cur.fetchall()
    li_box.delete(0, tk.END)  
    li_box1 = "\n".join([f"{row[0]}. {row[1]} - {row[2]}" for row in val_1]) if val_1 else "No Task available"
    if val_1:
        for item in li_box1.split("\n"):
            li_box.insert(tk.END, item)
    else:
        li_box.insert(tk.END, li_box1)



def up_task():  
    sel = li_box.curselection()
    if sel:
        task_id = li_box.get(sel).split('.')[0] 
        cur.execute("UPDATE tasks SET status=%s WHERE id=%s", ("Completed", task_id))  
        db.commit()
        show_tasks()
        messagebox.showinfo("Updated!", "Task marked as completed.")  

li_box = tk.Listbox(win, width=50, height=10)
li_box.pack(pady=10)

up_but = tk.Button(win, text="Mark as Completed", font=("Arial", 15), command=up_task)  
up_but.pack(pady=5)  

show_tasks()

win.mainloop()

