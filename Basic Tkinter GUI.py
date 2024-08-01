import tkinter as tk
root = tk.Tk()
root.maxsize(400, 400)
root.minsize(400, 400)
             
label_username = tk.Label(text ="Enter Username:")
label_username.pack()
enter_username = tk.Entry()
enter_username.pack()

label_password = tk.Label(text="Enter Password:")
label_password.pack()
enter_password = tk.Entry(show="*")
enter_password.pack()

result = tk.Label(root)
result.pack()

def Login():
    username = enter_username.get()
    password = enter_password.get()

    if username == "..." and password == "...":
        result.config(text="Access Granted!")
    else:
            result.config(text="Access Denied X")

login_button = tk.Button(text="Login", command=Login)
login_button.pack()


root.mainloop
