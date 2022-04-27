from tkinter import*
from server import *

main = Tk()
server = Server()

#Window
main.title("Chatbot 1IM")
main.geometry("400x520")
main.resizable(height=FALSE, width=FALSE)

#Icon
icon = PhotoImage(file = "Icon.png")
main.iconphoto(False, icon)

#Menu
main_menu = Menu(main)
file_menu = Menu(main)
main_menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New")
file_menu.add_command(label="Quit", command=main.destroy)
main_menu.add_command(label="Quit", command=main.destroy)
main.config(menu=main_menu)

#Chat
txtChat = Text(main, bg="#222230", foreground="#d1d2eb")
txtChat.place(x=6, y=6, height=418, width=367)

#Input
entInput = Entry(main, width=44, bg="#222230", foreground="#d1d2eb")
entInput.place(x=6, y=430, height=64)

WORDLIST = ["what", "hva", "ka", "hvilken", "kor", "where", "er", "is", "?", "a", "i", "in"] # bare simpel ordliste

#Send Text
def send():
    response_input = entInput.get()
    storedInput = "You> " + entInput.get()

    for x in response_input.split(): # removes uneccesary words from the bot
        x.lower()
        if x in WORDLIST:
            response_input = x.replace(x, "")
        else:
            lol = x


    response_input.replace(" ", "") # får vekk mellomrom
            
    txtChat.insert(END, "\n" + storedInput)
    answer = server.request(lol)
    answer = "\nBot> " + answer
    txtChat.insert (END, answer)

#Send Button
btnSend = Button(main, text=("SEND"), bg="#222230", font=("Times", "24", "bold"), foreground="#d1d2eb", activebackground="#d1d2eb",activeforeground="#222230", command=send)
btnSend.place(x=278,y=430)

#Scrollbar
scrollbar = Scrollbar(main, command=txtChat.yview, cursor="heart")
scrollbar.place(x=375, y=5, height = 420)

main.mainloop()