from tkinter import *
import csv
import sys

root = Tk()
root.title("Barcode Scanner")
root.geometry("300x200")
root.resizable(False, False)


# For the manufacturer drop down box
MANUFACTURER_OPTIONS = [
    "Seagate",
    "Western Digital",
    "Sandisk",
    "Maxtor",
    "Conner",
    "Hitachi",
    "Deskstar",
] 

manu_choice = StringVar()
manu_choice.set("Manufacturer")
drop = OptionMenu(root, manu_choice, *MANUFACTURER_OPTIONS)
drop.place(x=10,y=10)


# For the serial number
Label(root, text="Serial Number").place(x=15, y=45)
serial = Entry(root, width=20)
serial.place(x=100, y=45)


# For the Model number
Label(root, text="Model Number").place(x=15,y=70)
model_no = Entry(root, width=20)
model_no.place(x=105,y=70)


# For the storage size
Label(root, text="Size").place(x=15, y=100)
how_much = Entry(root, width=5)
how_much.place(x=45, y=100)


# For the different storage sizes
SIZES = ["GB", "MB", "TB"]

size_choice = StringVar()
size_choice.set(SIZES[0])
drop = OptionMenu(root, size_choice, *SIZES)
drop.place(x=75, y=95)


# Store all values
def store():
    name = manu_choice.get()
    size_value = how_much.get()
    size = size_choice.get()
    s_n = serial.get()
    mdl = model_no.get()

    with open (sys.argv[1], "a") as file:
        writer = csv.DictWriter (file, fieldnames=["Manufacturer Name", "MDL", "S/N", "SIZE"])
        writer.writerow({"Manufacturer Name":name, "MDL":mdl, "S/N":s_n, "SIZE":f"{size_value}{size}"}) 


def clear():
    manu_choice.set("Manufacturer")
    serial.delete(0,END)
    model_no.delete(0,END)
    how_much.delete(0, END)
    size_choice.set(SIZES[0])
    pass

Button(root, text="Save", command=store).place(x=30,y=150)
Button(root, text="Next", command = clear).place(x= 80,y=150)


root.mainloop()