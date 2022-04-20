from tkinter import Tk, Label, Button
from server import Server

tk = Tk()
server = Server()

# setup
tk.title("snorres chatbot")
tk.resizable(height= False, width = False)
tk.geometry("1290x720")

HEIGHT, WIDTH = 1290, 720

#logikk


# design

# small top-text so that people have basic instructions
lbl_intro = Label(text="Welcome to this chatbot!", fg="black", )
lbl_intro.config(font=("comic sans", 16))
lbl_intro.place(x = WIDTH/1.4, y = HEIGHT/53)

lbl_content = Label(text="You can ask me all your python related questions!", fg="black", )
lbl_content.config(font=("comic sans", 16))
lbl_content.place(x = WIDTH/1.8, y = HEIGHT/23)

btn_submit = Button(tk, bg="black")

tk.mainloop()