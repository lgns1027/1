from tkinter import *
import random
from tkinter import messagebox
num1=0
num2=0
num3=0

def pop():
    popup=Tk()
    popup.title=("축하합니다")
    popup.geometry("400x100")
    photo= PhotoImage(file="달러.png")
    label=Label(popup,image=photo ,width=80,height=80)
    label.place(x=300,y=350)
    popup.mainloop()

def slot1():
    global num1
    num1=random.randint(1,3)
    result1.configure(text=num1)
def slot2():
    global num2
    num2=random.randint(1,3)
    result2.configure(text=num2)    
def slot3():
    global num3
    global num1
    global num2
    num3=random.randint(1,3)
    result3.configure(text=num3)
    if (num1==num2) and (num2==num3) :
        messagebox.showinfo(title="축하",message="굿", )
    else :
        messagebox.showinfo(title="아쉽군요",message="떙",)




#윈도우 생성
root=Tk()
root.title("여행지 선발대 뽑기 프로그램")
root.geometry('500x500')
root.resizable(False,False)


#타이틀 레이블 생성
title=Label(root,text="슬롯머신",font=('맑은고딕',20,'bold'))
title.place(x=190,y=10)

#버튼
result1=Label(root,text="",width=9,height=5,font=("맑은고딕",11,"bold"),bg="white")
result1.place(x=100,y=150)

result2=Label(root,text="",width=9,height=5,font=("맑은고딕",11,"bold"),bg="white")
result2.place(x=200,y=150)

result3=Label(root,text="",width=9,height=5,font=("맑은고딕",11,"bold"),bg="white")
result3.place(x=300,y=150)

btn1=Button(root,text="",width=9,font=("굴림",11,"bold"),bg="red",fg="white",command=slot1)
btn1.place(x=100,y=300)

btn2=Button(root,text="",width=9,font=("굴림",11,"bold"),bg="yellow",fg="white",command=slot2)
btn2.place(x=200,y=300)

btn3=Button(root,text="",width=9,font=("굴림",11,"bold"),bg="green",fg="white",command=slot3)
btn3.place(x=300,y=300)



    
