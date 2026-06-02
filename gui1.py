import tkinter as tk

def check_login():
    user=user_entry.get()
    pwd=pwd_entry.get()
    
    if user=="admin" and pwd=="1234":
        msg_label.config(text="Login Successful!",fg="green")
    else:
        msg_label.config(text="Wrong password!",fg="red")
        
#window create
root=tk.Tk()
root.title("Secure login")

#label create
tk.Label(root,
         text="Username:").pack(pady=5)
user_entry=tk.Entry(root)
user_entry.pack()

tk.Label(root,
         text="Password:").pack(pady=5)

pwd_entry=tk.Entry(root,show="*")
pwd_entry.pack()

#button create
tk.Button(root,text="Login",
          command=check_login).pack(pady=15)

msg_label=tk.Label(root,text="")
msg_label.pack()

root.mainloop()
