from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Barcode Scanner")
root.geometry("150x300")

# For the manufacturer drop down box
MANUFACTURER_OPTIONS = [
    "Segate",
    "Western Digital",
    "Sandisk",
    "Maxtor"
] 

manu_choice = StringVar()
manu_choice.set("Manufacturer")
drop = OptionMenu(root, manu_choice, *MANUFACTURER_OPTIONS)
drop.pack()


# For the storage size
how_much = Entry(root, width=5)
how_much.pack()


# For the different storage sizes
SIZES = ["GB", "MB"]

size_choice = StringVar()
size_choice.set("Size")
drop = OptionMenu(root, size_choice, *SIZES)
drop.pack()



# Store all values
def myClick():
    store = Label(root, drop.get())
    store.pack
    print (store)

myButton = Button

root.mainloop()