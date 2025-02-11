import tkinter as tk
import random as rd  

k = tk.Tk()
k.geometry("400x500")
k.title("Rock-Paper-Scissor")
k.configure(bg="sky blue")

us_sc = 0
pc_sc = 0

l1 = tk.Label(k, text="Computer Choice: ", font=("Arial", 15))
l1.pack(pady=10)

l2 = tk.Label(k, text="Your Score: 0", font=("Arial", 15))
l2.pack(pady=10)

l3 = tk.Label(k, text="Computer Score: 0", font=("Arial", 15))
l3.pack(pady=10)

l4 = tk.Label(k, text="Winner: ?", font=("Arial", 20), fg="red")
l4.pack(pady=20)

def pl_r():
    pl("Rock")

def pl_p():
    pl("Paper")

def pl_s():
    pl("Scissors")

def pl(us_ch):
    global us_sc, pc_sc

    options = ["Rock", "Paper", "Scissors"]
    com_ch = rd.choice(options)
    l1.config(text=f"Computer Choice: {com_ch}")

    if us_ch == com_ch:
        result = "It's a Tie!"
    elif (us_ch == "Rock" and com_ch == "Scissors") or \
         (us_ch == "Scissors" and com_ch == "Paper") or \
         (us_ch == "Paper" and com_ch == "Rock"):
        result = "You Win!"
        us_sc += 1
    else:
        result = "Computer Wins!"
        pc_sc += 1

    l2.config(text=f"Your Score: {us_sc}")
    l3.config(text=f"Computer Score: {pc_sc}")
    l4.config(text=f"Winner: {result}")

b1 = tk.Button(k, text="Rock", font=("Arial", 15), command=pl_r)
b1.pack(pady=5)

b2 = tk.Button(k, text="Paper", font=("Arial", 15), command=pl_p)
b2.pack(pady=5)

b3 = tk.Button(k, text="Scissors", font=("Arial", 15), command=pl_s)
b3.pack(pady=5)

def rst_gm():
    global us_sc, pc_sc
    us_sc = 0
    pc_sc = 0
    l2.config(text="Your Score: 0")
    l3.config(text="Computer Score: 0")
    l4.config(text="Winner: ?")

b4 = tk.Button(k, text="Reset", font=("Arial", 15), bg="red", fg="white", command=rst_gm)
b4.pack(pady=10)

k.mainloop()
