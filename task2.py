from tkinter import*
root=Tk()
root.title("task2")
root.geometry('250x150')
fr1=Frame(root)
fr1.pack(side=TOP,fill=BOTH)
btn1=Button(fr1,text='Ok_1', width=5,height=1)
btn1.pack(side=LEFT)
btn2=Button(fr1,text='Ok_2', width=5,height=1)
btn2.pack(side=RIGHT)
fr2=Frame(root)
fr2.pack(side=BOTTOM,fill=BOTH)
btn3=Button(fr2,text='Ok_3', width=5,height=1)
btn3.pack(side=LEFT)
btn4=Button(fr2,text='Ok_4', width=5,height=1)
btn4.pack(side=RIGHT)
root.mainloop()
