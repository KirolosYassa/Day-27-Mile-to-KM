from tkinter import *

window = Tk()

window.title("Desktop App") 
window.minsize(width=500, height=300)

def got_clicked():
    input_answer = input_field.get()
    print(input_answer)
    
    
lbl = Label(text="Hello World!", font=("Arial", 24, "bold"))
lbl.grid(column=0, row=0)

btn = Button(text="Click Me!", command=got_clicked)
btn.grid(column=1, row=1)

newBtn = Button(text="new Button", command=got_clicked)
newBtn.grid(column=2, row=0)

input_field = Entry(text="", width=10)
input_field.grid(column=3, row=2)



window.mainloop()