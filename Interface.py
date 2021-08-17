from tkinter import *

app = Tk()
app.configure(bg="orange")

def informatienaamrandom():
    info = Label(app, text="hallo " + input.get())
    info.grid(row=2, column=1)

DIT = Button(app, text="Your name?", fg="red", bg="#39FF14",borderwidth=50, font=('Helvetica', 18, 'bold'), command=informatienaamrandom)
DIT.grid(row=1, column=1)

input = Entry(app)
input.grid(row=6, column=3)

check = Checkbutton(app, text="data")
check.grid(row=8,column=10)

naamlijst = StringVar(app)
naamlijst.set("Kies een naam")
menu = OptionMenu(app, naamlijst, "Sofie", "Saar", "Tine")
menu.grid(row=10,column=1)

app.mainloop()
