import tkinter as tk
from turtle import position, window_height, window_width

root = tk.Tk()
root.title("Tkinter Window- Center")
root.geometry("600x400+50+50")
root.resizable(False, False)
# message =tk.Label(root,  text="Hello, World!")
# message.pack()
# get the screen dimension
# screen_width = root.winfo_screenwidth()
# screen_height = root.winfo_screenheight()

# # find the center point
# center_x= int(screen_width/2 - window_width/2)
# center_y = int(screen_height/2 - window_height/2)

# # set the position of the window to the center of the screen
# root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
root.mainloop()


