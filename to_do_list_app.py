import tkinter as tk

tasks = []

def add_task():
    task = task_entry.get()   #takes input from the user
    if task :
        var = tk.BooleanVar()
        chk =tk.Checkbutton(task_frame,text=task, variable=var,font =("Arial",12,"bold"))
        chk.pack(anchor="w")
        tasks.append((chk,var))
        task_entry.delete(0,tk.END)

def remove_task():
    for chk,var in tasks[:] :
        if var.get():
            chk.destroy()
            tasks.remove((chk,var))

#Create a main window
root = tk.Tk()
root.title("Let's make a To-do list") 
root.geometry("500x450")


#Create a label
title_label = tk.Label(root,text = "My To-Do List", font=("Arial",20,"bold"))
title_label.pack(pady=20)

task_entry = tk.Entry(root, width=30)
task_entry.pack(pady=10)

# Frame to hold tasks (checkboxes)
task_frame=tk.Frame(root)
task_frame.pack(pady=10)

#create a button
button_frame =tk.Frame(root)
button_frame.pack()

tk.Button(button_frame,text="Add Task",command=add_task,font=("Arial",14,"bold"), fg="yellow",bg="brown",bd =4).grid(row=0,column=0,padx=10)
tk.Button(button_frame,text="Remove Task",command=remove_task,font=("Arial",14,"bold"), fg="yellow",bg="brown",bd =4).grid(row=0,column=1,padx=10)


#start the main loop
root.mainloop()

