from tkinter import Tk, Label
from server import Server

tk = Tk()
server = Server()

# setup
tk.title("snorres chatbot")
tk.resizable(height= False, width = False)
tk.geometry("500x500")

HEIGHT, WIDTH = 500, 500

# design
x = Label(text="Test", fg="black", bg="white")
x.place(x = HEIGHT/2, y = WIDTH/2)

tk.mainloop()