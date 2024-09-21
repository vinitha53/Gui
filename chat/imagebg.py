import tkinter as tk
from PIL import Image, ImageTk

# Create the main window
root = tk.Tk()
root.title("Background Image Example")

# Load the image with Pillow
pil_image = Image.open("C:/Users/god/Desktop/ff.jpg")
img = ImageTk.PhotoImage(pil_image)

# Create a canvas widget
canvas = tk.Canvas(root, width=pil_image.width, height=pil_image.height)
canvas.pack(fill="both", expand=True)

# Add the image to the canvas as the background
canvas.create_image(0, 0, image=img, anchor="nw")

# Optionally add other widgets on top of the background
label = tk.Label(root, text="Hello, World!", font=("Arial", 10), bg="white")
label.place(x=0, y=0)
tbInputValue1=tk.Entry(root)
tbInputValue1.place(x=60,y=50)

# Keep a reference to the image to avoid garbage collection
canvas.image = img

# Start the Tkinter event loop
root.mainloop()
