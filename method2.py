# Windows 11, Python 3.10.4, Tkinter 8.6

# necessary imports
from tkinter import *
from tkinter import ttk
from tkinter.ttk import Combobox

# initialization
root = Tk()
width=800
height=1020
root.geometry(str(width)+"x"+str(height)+"+10+10")

# creating a scrolling canvas frame
main_frame = Frame(root,width=width,height=height)
main_frame.place(x=0,y=0)
canvas = Canvas(main_frame, width=width, height=height)
canvas.place(x=0,y=0)
scrolly = ttk.Scrollbar(main_frame, orient=VERTICAL, command=canvas.yview)
scrolly.place(x=width-15,y=0,height=height)
canvas.configure(yscrollcommand=scrolly.set)
canvas.bind('<Configure>', lambda e: canvas.configure(scrollregion = canvas.bbox("all")))
def _on_mouse_wheel(event):
    if isinstance(event.widget, str): # String because it does not have an actual reference
        if event.widget.endswith('.!combobox.popdown.f.l'): # If it is the listbox
            return 'break'
    canvas.yview_scroll(-1 * int((event.delta / 120)), "units") # Else scroll the canvas
    w.event_generate('<Escape>') # Close combobox
    #w.event_generate('<Escape>') # close the combobox listbox component if the mouse stops hovering over it
canvas.bind_all("<MouseWheel>", _on_mouse_wheel)
w = Frame(canvas,width=width,height=height)
w.place(x=0,y=0)
canvas.create_window((0,0), window=w, anchor="nw")
w.configure(height=3000)

# combobox initialization
sel = Combobox(w, values=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20])
sel.place(x=10, y=10)

# tkinter mainloop
root.mainloop()
