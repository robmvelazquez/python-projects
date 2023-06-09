import tkinter as tk
import PyPDF2
from PIL import Image, ImageTk

root = tk.Tk()

canvas = tk.Canvas(root, width=600, height=300)
canvas.grid(columnspan=3)

# Logo
logo = Image.open('logo.jpg')
logo = ImageTk.PhotoImage(logo)
logo_label = tk.Label(image=logo)
logo_label.image = logo
logo_label.grid(column=1, row=0)

# Instructions
instructions = tk.Label(root, text='Select a PDF to extract text: ', font='Raleway')
instructions.grid(columnspan=3, column=0, row=1)

root.mainloop()