import tkinter as tk

window=tk.Tk()
window.geometry('500x500')
window.title('Grid')

myframe=tk.Frame(window)
myframe.columnconfigure(0,weight=5)
myframe.columnconfigure(1,weight=2)

b1=tk.Button(myframe,text='B1',foreground='green')
b1.grid(row=0,column=0,sticky='we')

b2=tk.Button(myframe,text='B2')
b2.grid(row=0,column=1,sticky='we')

b3=tk.Button(myframe,text='B3')
b3.grid(row=1,column=0,sticky='we')

b4=tk.Button(myframe,text='B4')
b4.grid(row=1,column=1,sticky='we')


myframe.pack(fill='x')

mylabel=tk.Label(window,text='Text field',foreground='yellow',background='blue',font=('Arial',18),height=1)
mylabel.pack(side='top',padx=20,pady=5,ipadx=2,ipady=2)

mytext=tk.Text(window)
mytext.pack(padx=20,pady=2,side='bottom')

window.mainloop()

