import tkinter as tk
root=tk.Tk()

root.geometry("500x500")
root.title('Gogo ...')

label=tk.Label(root,text='Files ...',font=('Arial',18))
label.pack(padx=20,pady=20)

text=tk.Text(root,font=('Arial',16),height=3)
text.pack(padx=100)

myentry=tk.Entry(root)
myentry.pack(fill='x')


root.mainloop()
