import tkinter as tk


window = tk.Tk()
frame = tk.Frame()
label = tk.Label(master=frame, text="I'm in Frame A")
label.pack()

frame.pack()

window.mainloop()