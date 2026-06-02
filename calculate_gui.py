import tkinter as tk

def calculate_si():
    
    p=float(p_entry.get())
    r=float(r_entry.get())
    t=float(t_entry.get())
    
    si=(p*r*t)/100
    res_label.config(text=f"Simple Intrest:{si}",fg="blue")
    
root=tk.Tk()
root.title("SI Calculator")
root.geometry("300x250")

tk.Label(root,text="Principal (P):").grid(row=0,column=0,padx=10,pady=5)

p_entry=tk.Entry(root)
p_entry.grid(row=0,column=1)

tk.Label(root,text="rate (R%):").grid(row=1,column=0,padx=10,pady=5)
r_entry=tk.Entry(root)
r_entry.grid(row=1,column=1)

tk.Label(root,text="Time (T yrs):").grid(row=2,column=0,padx=10,pady=5)
t_entry=tk.Entry(root)
t_entry.grid(row=2,column=1)

btn=tk.Button(root,text="Calculate", command=calculate_si,bg="orange")
btn.grid(row=3,columnspan=2,pady=20)

res_label=tk.Label(root,text="Result",font=("Arial",10,"bold"))
res_label.grid(row=4,columnspan=2)

root.mainloop()