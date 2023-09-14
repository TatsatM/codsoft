from tkinter import *
root=Tk()
root.geometry("600x450")
root.title("TO DO LIST")
root.minsize(570,0)

          # for add a task
def AddTasks():
    content=userentry.get(1.0,END)
    listtask.insert(END,content)
    with open('task.txt',"a") as file:
        file.write(content)
        file.seek(0)
        file.close()
    userentry.delete(1.0,END)

    #for delete a task
def DeleteTasks():
    delete=listtask.curselection()
    look=listtask.get(delete)
    listtask.delete(delete)
    with open("task.txt","r") as f:
        nf=f.readlines()
    with open("task.txt","w") as f:
        for line in nf:
            if line.strip() not in look:
                f.write(line)
        f.truncate()


label=Label(root,text="Welcome to  ' TO DO LIST ' ",bg="orange", padx=1000, pady=3,font=("Algerian",20,"bold"))
label.pack()

entervalue=Label(root,text="Enter Tasks",font=("TimesNewRoman",15),bg="black",fg="white")
entervalue.place(x=30,y=57)

#for to take user input into the textbox
userentry=Text(root,height=3,width=20,)
userentry.place(x=20,y=106)

# button for adding task
Button(text="Add Tasks",command=AddTasks,bg="#C1FFC1").place(x=10,y=150)

value=Label(root,text="Task list",font=("TimesNewRoman",15),bg="black",fg="white")
value.place(x=300,y=60)

listtask=Listbox(root,width=30,height=16,fg="red")
listtask.place(x=300,y=106)

Button(text="Delete Tasks",command=DeleteTasks,bg="#C1FFC1").place(x=300,y=390)

root.mainloop()