#VERSION 5

import tkinter as tk
root = tk.Tk()
headline = tk.Label(text="LOGIN TO DISCORD", bg="#b1f2ff", font = 80)
headline.pack()
root.maxsize(350, 350)
root.minsize(350, 350)
root.config(bg="#b1f2ff")
             
label_username = tk.Label(text ="Enter Username:", bg="#b1f2ff")
label_username.pack()
enter_username = tk.Entry()
enter_username.pack()

label_password = tk.Label(text="Enter Password:", bg="#b1f2ff")
label_password.pack()
enter_password = tk.Entry(show="*")
enter_password.pack()

result = tk.Label(root)
result.pack()

def Login():
    username = enter_username.get()
    password = enter_password.get()

    if username == "chocopie" and password == "360":
        result.config(text="Access Granted!", fg="green", bg="#b1f2ff")
    else:
            result.config(text="Access Denied X", fg="red", bg="#b1f2ff")

login_button = tk.Button(text="Login", command=Login)
login_button.pack()


root.mainloop

# replace ("chocopie" and "360") with the username and password that you want to set
