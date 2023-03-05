import tkinter as tk


def importRep():
    print(fileEntry.get())

window=tk.Tk()
window.geometry('900x650')
window.title('Report Importer')


#Frame #1 --------------
myframe1=tk.LabelFrame(window,text='Input')


myframe1.columnconfigure(0,weight=5)
myframe1.columnconfigure(1,weight=1)

inputLabel=tk.Label(myframe1,text='Input Files (mask)',font=('Arial',12),height=1)
inputLabel.grid(row=0,column=0,sticky='w')

fileEntry=tk.Entry(myframe1,font=('Currier',12))
fileEntry.grid(row=1,column=0,sticky='we')

pinCheck=tk.Checkbutton(myframe1,text='Default',height=1)
pinCheck.grid(row=1,column=1,sticky='we')

importButton=tk.Button(myframe1,text='Import Files',command=importRep)
importButton.grid(row=2,column=0)

#Frame #2 ---------------
myframe2=tk.LabelFrame(window,text='Console')
myframe2.columnconfigure(0,weight=5)
myframe2.columnconfigure(1,weight=1)

importedLabel=tk.Label(myframe2,text='Imported',font=('Arial',12),height=1)
importedLabel.grid(row=0,column=0)

myText=tk.Text(myframe2,font=('Currier',12))
myText.grid(row=1,column=0,sticky='nswe')


#Packing
myframe1.pack(fill='x',padx=20,pady=20)
myframe2.pack(fill='x',padx=20)


window.mainloop()

