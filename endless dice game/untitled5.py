from tkinter import*
import random
from PIL import ImageTk,Image
root=Tk()

root.title("Endless dice game")
root.geometry("500x500")
root.configure(background="green")

img=ImageTk.PhotoImage(Image.open("dice1.4.jpg"))

p1_label=Label(root,text="Player 1",bg="purple",fg="white")
p1_label.place(relx=0.2,rely=0.3,anchor=CENTER) 

p2_label=Label(root,text="Player 2",bg="purple",fg="white")
p2_label.place(relx=0.8,rely=0.3,anchor=CENTER)

s1_label=Label(root,bg="orange")
s1_label.place(relx=0.2,rely=0.4,anchor=CENTER)

s2_label=Label(root,bg="orange")
s2_label.place(relx=0.8,rely=0.4,anchor=CENTER)

show_label=Label(root,bg="red",fg="white")
show_label.place(relx=0.5,rely=0.5,anchor=CENTER)

p1Score=0

def pl1Score():
    global p1Score
    Score=random.randint(1,6)
    show_label["text"]="the Player 1 dice number is " +str (Score)
    p1Score=p1Score+Score
    s1_label["text"]=str(p1Score)
    
btn_1=Button(root,image=img,command=pl1Score) 
btn_1.place(relx=0.2,rely=0.7,anchor=CENTER)

p2Score=0

def pl2Score():
    global p2Score
    score=random.randint(1,6)
    show_label["text"]="The Player 2 dice number is "+str (score)
    p2Score=p2Score+score
    s2_label["text"]=str (p2Score)
    
btn_2=Button(root,image=img,command=pl2Score) 
btn_2.place(relx=0.8,rely=0.7,anchor=CENTER)   
   
root.mainloop()

