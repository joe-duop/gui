from tkinter import *

# creating the main widget
rootWidget = Tk()
rootWidget.title("Simple Calc")

# the input field
entryWidget = Entry(rootWidget, width=35, borderwidth=5)
entryWidget.grid(row=0, column=0, columnspan=3, padx=10, pady=10)


def button_click(number):
    current = entryWidget.get()  # getting the number entered
    entryWidget.delete(0, END)  # deleting the current number so it doesnt repeat itself
    return entryWidget.insert(0, str(current) + str(number))  # modified to take more than 2-digit number

def button_clear():
    entryWidget.delete(0, END)  # clears the input field


def button_add(number):
    current = entryWidget.get()
    entryWidget.delete(0, END)
    entryWidget.insert(0, str(current) + str(number))


# creating the buttons
button1 = Button(rootWidget, text="1", padx=40, pady=20, command=lambda: button_click(1))
button2 = Button(rootWidget, text="2", padx=40, pady=20, command=lambda: button_click(2))
button3 = Button(rootWidget, text="3", padx=40, pady=20, command=lambda: button_click(3))
button4 = Button(rootWidget, text="4", padx=40, pady=20, command=lambda: button_click(4))
button5 = Button(rootWidget, text="5", padx=40, pady=20, command=lambda: button_click(5))
button6 = Button(rootWidget, text="6", padx=40, pady=20, command=lambda: button_click(6))
button7 = Button(rootWidget, text="7", padx=40, pady=20, command=lambda: button_click(7))
button8 = Button(rootWidget, text="8", padx=40, pady=20, command=lambda: button_click(8))
button9 = Button(rootWidget, text="9", padx=40, pady=20, command=lambda: button_click(9))
button0 = Button(rootWidget, text="0", padx=40, pady=20, command=lambda: button_click(0))
buttonAdd = Button(rootWidget, text="+", padx=40, pady=20, command=lambda: button_add("+"))
buttonEqual = Button(rootWidget, text="=", padx=80, pady=20, command=button_click)
buttonClear = Button(rootWidget, text="Clear", padx=80, pady=20, command=button_clear)

# arranging the buttons on the screen
button1.grid(row=3, column=0)
button2.grid(row=3, column=1)
button3.grid(row=3, column=2)

button4.grid(row=2, column=0)
button5.grid(row=2, column=1)
button6.grid(row=2, column=2)

button7.grid(row=1, column=0)
button8.grid(row=1, column=1)
button9.grid(row=1, column=2)

button0.grid(row=4, column=0)
buttonClear.grid(row=4, column=1, columnspan=2)
buttonAdd.grid(row=5, column=0)
buttonEqual.grid(row=5, column=1, columnspan=2)

# running the main widget
rootWidget.mainloop()

# creating the buttons
# numberButtons = {}
# for i in range(1, 10):
#     btn = Button(rootWidget,
#                  text=i,
#                  padx=40,
#                  pady=20,
#                  command=button_add)
#     numberButtons["button" + str(i)] = btn
# numberButtons["button" + str(0)] = 0

# arranging the buttons on the screen
