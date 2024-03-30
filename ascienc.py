from tkinter import *

root = Tk()

root.title("ASCII")
root.geometry("400x400")
root.configure(background = "light blue")


enter_name = Entry(root)
enter_name.place(relx=0.5,rely=0.4,anchor=CENTER)

label = Label(root, text = "Your name in ASCII is: ", bg="light yellow", fg="black")
encryp = Label(root, text = "Your encrypted characters are: ", bg="light yellow", fg="black")

def ASCIIconverter():
    input_name = enter_name.get()
    
    for letter in input_name :
        label["text"] += str(ord(letter)) + " "
        enc = int(ord(letter)) - 1
        encryp["text"] += str(chr(enc))
        
    
btn=Button(root, text="Show ASCII name and encrypt", command=ASCIIconverter, bg='gold',  fg = 'black')
btn.place(relx=0.5, rely=0.5, anchor=CENTER)

label.place(relx=0.5, rely= 0.6, anchor=CENTER)
encryp.place(relx=0.5, rely= 0.7, anchor=CENTER)

root.mainloop()
 
