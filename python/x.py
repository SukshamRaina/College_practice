import tkinter as tk
root=tk.Tk() #creating a window
root.title("My First GUI") #setting the title of the window
label = tk.Label(root,text="Form") #creating a label widget
label.grid(row=0,column=0,columnspan=2) #placing the label widget in the window using grid layout

label = tk.Label(root,text="Enter your name:") #creating a label widget
label.grid(row=1,column=0) #placing the label widget in the window using grid layout

entry = tk.Entry(root)  #creating an entry widget for user input
entry.grid(row=1,column=1)  #placing the entry widget in the window using grid layout
#pack() is used to organize the widgets in blocks before placing them in the parent widget.

button = tk.Button(root,text="Start")   #creating a button widget with the text "Start"
button.grid(row=2,column=0,columnspan=2)  #placing the button widget in the window using grid layout


root.mainloop() #to keep the window open