from tkinter import*
root=Tk()
root.title("tk #2")
root.geometry('250x300')
fr1=Frame(root)
fr1.pack(side=TOP,fill=BOTH)
btn1=Button(fr1,text='1', width=6,height=2)
btn1.pack(side=LEFT)
btn3=Button(fr1,text='3', width=6,height=2)
btn3.pack(side=RIGHT)
fr2=Frame(root)
fr2.pack(anchor=N)
btn2=Button(fr2, text='2', width=6,height=2)
btn2.pack()
fr3=Frame(root)
fr3.pack(side=BOTTOM, fill=BOTH)
btn5=Button(fr3, text='5', width=6,height=2)
btn5.pack(side=RIGHT)
btn4=Button(fr3, text='4', width=6,height=2)
btn4.pack(anchor=E,padx=15)
root.mainloop()
