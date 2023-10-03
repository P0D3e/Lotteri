from tkinter import *
from tkinter import messagebox
import lotteri

root = Tk()
root.title("Lotteri")

listbox = Listbox(root, height=4,
                  width=30,
                  bg="white",
                  activestyle='dotbox',
                  font="Helvetica",
                  fg="blue")

root.geometry("380x300")
lotteriet = lotteri.Lotteri()

label_antal = Label(root, text="Antal Lotter, max 3st:")
label_antal.grid(row=0, column=0, sticky=E, padx=5, pady=5)

textbox_antal = Entry(root, width=2)
textbox_antal.grid(row=0, column=1, sticky=W, padx=5, pady=5)
textbox_antal.focus_set()


def update_listbox(antal_lotter):
    listbox.delete(0, END)
    listbox.insert(1, "Grattis du vann det här!")


def clickSlumpaButton():
    try:
        antal_lotter = int(textbox_antal.get())
        i = 0
        if antal_lotter < 4:
            while i < antal_lotter:
                vinst = lotteriet.get_vinst()
                listbox.insert(i + 2, vinst)
                i += 1
        else:
            messagebox.showinfo("Fel antal lotter", "Du har valt för många lotter!")
    except ValueError:
        messagebox.showinfo("Felaktig inmatning", "Endast siffror tillåtna!")


slumpa_button = Button(root, text="Slumpa lotter", command=clickSlumpaButton)
slumpa_button.grid(row=1, column=0, columnspan=2, pady=10)

listbox.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

root.mainloop()
