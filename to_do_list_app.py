import tkinter as tk


def add_task():
    task = task_entry.get()   #takes input from the user
    if task :
        listbox.insert(tk.END, f"• {task}")  # shows the list of tasks 
        task_entry.delete(0,tk.END)

def remove_task():
    selected_task =listbox.curselection() # get selected item index
    if selected_task :
        listbox.delete(selected_task[0]) # deletes that item

#Create a main window
root = tk.Tk()
root.title("Let's make a To-do list") 
root.geometry("500x450")


#Create a label
title_label = tk.Label(root,text = "My To-Do List", font=("Arial",20,"bold"))
title_label.pack(pady=20)

listbox = tk.Listbox(root, width=40, height=10, font=("Arial", 12))
listbox.pack(pady=20)

task_entry = tk.Entry(root, width=30)
task_entry.pack(pady=10)

#craete a button
button_frame =tk.Frame(root)
button_frame.pack()

tk.Button(button_frame,text="Add task",command=add_task,font=("Arial",14,"bold"), fg="yellow",bg="green").grid(row=0,column=0,padx=10)
tk.Button(button_frame,text="Remove",command=remove_task,font=("Arial",14,"bold"), fg="yellow",bg="green").grid(row=0,column=1,padx=10)


#start the main loop
root.mainloop()
