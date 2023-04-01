from tkinter import Tk, Label, Button, Entry

# creating the main widget
rootWidget = Tk()

# creating a label and placing in the root folder
labelWidget = Label(rootWidget, text="hello world")
labelWidget.pack()

# input field
entryWidget = Entry(rootWidget)
entryWidget.insert(0, "Type in your password")  # the text will be displayed inside the input space
entryWidget.pack()


# what to do after clicking funtion
def after_click():
    txt = entryWidget.get()  # gets the text that was entered in the entry widget
    txt = txt.lower()  # making the text lowercase
    if txt == "joe":
        theText = "welcome back " + txt
        Label(rootWidget, text=theText).pack()
    else:
        theText = "you are not suppose to be here"
        Label(rootWidget, text=theText).pack()


# creating a button
myButton = Button(rootWidget,
                  text="Enter",  # the buttons name
                  # state="disabled",  # if you click nothing will happen if it were supposed to
                  command=after_click,  # calls a function after clicking the button
                  padx=50,  # increased the side margins
                  pady=10,  # increase top bottom margins
                  fg="blue",  # text color is turned to blue
                  bg="red")  # background of the button is changed to red
myButton.pack()

# exiting the programme
# use .destroy as a field not method
quitButton = Button(rootWidget,
                    text="exit program",
                    command=rootWidget.destroy
                    )
quitButton.pack()

# running the main widget
rootWidget.mainloop()

# # complete and working well
