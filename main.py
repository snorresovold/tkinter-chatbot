from tkinter import Tk, Label
from server import Server

tk = Tk()
server = Server()

# setup
tk.title("snorres chatbot")
tk.resizable(height= False, width = False)
tk.geometry("1290x720")

HEIGHT, WIDTH = 1290, 720

# design
intro = Label(text="Welcome to this chatbot!", fg="black", )
intro.config(font=("comic sans", 16))
intro.place(x = WIDTH/1.4, y = HEIGHT/53)

content = Label(text="You can ask me all your python related questions!", fg="black", )
content.config(font=("comic sans", 16))
content.place(x = WIDTH/1.8, y = HEIGHT/23)

tk.mainloop()