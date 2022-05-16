from tkinter import*
import random
from PIL import Image,ImageTk
root=Tk()
root.title("poka")
root.geometry("600x400")
root.configure(background="black")

img = ImageTk.PhotoImage(Image.open("Dice.jpg"))
pica = ImageTk.PhotoImage(Image.open("pikachu.jpg"))

label1=Label(root,text="Player1",bg="#345beb",fg="white")
label1.place(relx = 0.1, rely =0.2, anchor = CENTER)
label3=Label(root,bg="#ff0000",fg="white")
label3.place(relx = 0.1, rely =0.3, anchor = CENTER)

label5=Label(root,image=pica,bg="#ff7300",fg="white")
label5.place(relx = 0.5, rely =0.5, anchor = CENTER)

label2=Label(root,text="Player2",bg="#345beb",fg="white")
label2.place(relx = 0.9, rely =0.2, anchor = CENTER)
label4=Label(root,bg="#ff0000",fg="white")
label4.place(relx = 0.9, rely =0.3, anchor = CENTER)

button1=Button(root,image=img,anchor = CENTER)
button1.place(relx = 0.1, rely =0.5, anchor = CENTER)

button2=Button(root,image=img,anchor = CENTER)
button2.place(relx = 0.9, rely =0.5, anchor = CENTER)

root.mainloop()