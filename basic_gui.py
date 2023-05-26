import tkinter as tk

# Create the main window
window = tk.Tk()

# Set the window title
window.title("GUI Example")

# Create a label widget
label = tk.Label(window, text="Hello, GUI!")
label.pack()

# Create a button widget
button = tk.Button(window, text="Click Me!")
button.pack()

# Run the main event loop
window.mainloop()