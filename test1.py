import tkinter as tk

window = tk.Tk()
greeting = tk.Label(text="Hello, Tkinter")
label = tk.Label(
    text="Hello, Tkinter",
    foreground="white",  # Set the text color to white
    background="black"  # Set the background color to black
)
label_1 = tk.Label(text="Hello, Tkinter", background="#34A2FE")
label_2 = tk.Label(text="Hello, Tkinter", fg="white", bg="black")
label_3 = tk.Label(
    text="Hello, Tkinter",
    fg="white",
    bg="black",
    width=10,
    height=10
)

button = tk.Button(
    text="Click me!",
    width=25,
    height=5,
    bg="blue",
    fg="yellow",
)

entry = tk.Entry(fg="yellow", bg="blue", width=50)


label_10 = tk.Label(text="Hello")

# Retrieve a label's text
text = label_10["text"]

# Set new text for the label
label_10["text"] = "Good bye"



greeting.pack()
label.pack()
label_1.pack()
label_2.pack()
label_3.pack()
button.pack()
entry.pack()

window.mainloop()

