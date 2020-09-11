#%%
from tkinter import *
import winsound
import time


root=Tk()
root.geometry('500x500')
root.title("Morse Code Generator")

list=[]

def sub():
    a=str(entry1.get())
    for i in range(len(a)):
        if a[i]=="a" or a[i]=="A":
            list.append(".-")
        elif a[i]=="b" or a[i]=="B":
            list.append("-...")
        elif a[i]=="c" or a[i]=="C":
            list.append("-.-.")
        elif a[i]=="d" or a[i]=="D":
            list.append("-..")
        elif a[i]=="e" or a[i]=="E":
            list.append(".")
        elif a[i]=="f" or a[i]=="F":
            list.append("..-.")
        elif a[i]=="g" or a[i]=="G":
            list.append("--.")
        elif a[i]=="h" or a[i]=="H":
            list.append("....")
        elif a[i]=="i" or a[i]=="I":
            list.append("..")
        elif a[i]=="j" or a[i]=="J":
            list.append(".---")
        elif a[i]=="k" or a[i]=="K":
            list.append("-.-")
        elif a[i]=="l" or a[i]=="L":
            list.append(".-..")
        elif a[i]=="m" or a[i]=="M":
            list.append("--")
        elif a[i]=="n" or a[i]=="N":
            list.append("-.")
        elif a[i]=="o" or a[i]=="O":
            list.append("---")
        elif a[i]=="p" or a[i]=="P":
            list.append(".--.")
        elif a[i]=="q" or a[i]=="q":
            list.append("--.-")
        elif a[i]=="r" or a[i]=="R":
            list.append(".-.")
        elif a[i]=="s" or a[i]=="S":
            list.append("..")
        elif a[i]=="t" or a[i]=="T":
            list.append("-")
        elif a[i]=="u" or a[i]=="U":
            list.append("..-")
        elif a[i]=="v" or a[i]=="V":
            list.append("...-")
        elif a[i]=="w" or a[i]=="W":
            list.append(".--")
        elif a[i]=="x" or a[i]=="X":
            list.append("-..-")
        elif a[i]=="y" or a[i]=="Y":
            list.append("-.--")
        elif a[i]=="z" or a[i]=="Z":
            list.append("--..")
        elif a[i]== " ":
            list.append("/")
        else:
            list.append("#")
        list.append(" ")
    str1 = ''.join(list)
    list.clear()
    return str1

def show():
    x=sub()
    label.config(text=x)


def play():
    x=sub()
    for i in range(len(x)):
        if x[i]==".":
            winsound.PlaySound('dot.wav',winsound.SND_ASYNC)
        elif x[i]=="-":
            winsound.PlaySound('dash.wav',winsound.SND_ASYNC)
        else:
            time.sleep(0.8)

        time.sleep(0.4)
        

butt1=Button(root,text="Submit",command=sub)
butt1.place(x=180,y=130)    

butt2=Button(root,text="Show Morse Code",command=show)
butt2.place(x=180,y=200)
        
    
butt3=Button(root,text="|>Play Morse Code",command=play)
butt3.place(x=180,y=400)
      

name1=Label(root,text="Type Text")
name1.place(x=0,y=10)
entry1=Entry()
entry1.place(x=300,y=10)


label=Label(root,text="")
label.place(x=50,y=250)


mainloop()


    


