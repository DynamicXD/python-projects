from tkinter import *
from functools import partial


def validate(u, p):
    print(f"Username: {u.get()}")
    print(f"Password: {p.get()}")
    return


root = Tk()
root.geometry("400x150")
root.title("Login")

Label(root, text="Username").grid(row=0, column=0)
username = StringVar()
Entry(root, textvariable=username).grid(row=0, column=1)

Label(root, text="Password").grid(row=1, column=0)
password = StringVar()
Entry(root, textvariable=password, show="*").grid(row=1, column=1)

validate = partial(validate, username, password)

Button(root, text="Login", command=validate).grid(row=4, column=4)

root.mainloop()
