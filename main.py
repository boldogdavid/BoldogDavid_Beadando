from tkinter import *
import ado_szamol

def indul():
    netto.insert(END, str(ado_szamol.nettok(int(ber.get()))))
    osszado.insert(END, str(ado_szamol.adok(int(ber.get()))))



window = Tk()
window.title("Adó számolás!")
Label(window,text = "bruttó bér").grid(row = 0,column = 0)

ber = Entry(window, width=10 )
ber.grid(row=1,column=0)
Button(window, text="Számol", command=indul).grid(row=2,column=0)

Label(window,text="nettó bér").grid(row=3,column=0)
netto=Entry(window)
netto.grid(row=4,column=0)

Label(window,text="össz adó érték").grid(row=5,column=0)
osszado = Entry(window)
osszado.grid(row=6,column=0)

window.mainloop()

