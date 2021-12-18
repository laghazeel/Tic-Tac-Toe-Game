# Tic Tac Toe game  programmed by Laghzal Mouad


# Import dependencies
from tkinter import *
from TICTATOE import *
from PIL import Image
from PIL import ImageTk
# main function
def play():
    menu = Tk() 
    menu.geometry("600x600")
    menu.title("Tic Tac Toe by Laghazeel.")
      
    wpc = partial(withpc, menu)
    wpl = partial(withplayer, menu)

    head = Button(menu, text=" Hola ! let's play ",
                  activeforeground='gray',
                  activebackground="blue", bg="orange",
                  fg="black", width=500, height=5, font=('Arial Bold', 14), bd=5)

    B1 = Button(menu, text="Play with PC ", command=wpc,
                activeforeground='blue',
                activebackground="blue", bg="gray",
                fg="orange", width=500, height=5, font=('Arial Bold', 14), bd=5)

    B2 = Button(menu, text="Play with a Friend", command=wpl, activeforeground='orange',
                activebackground="gray", bg="orange", fg="gray",
                width=500, height=5, font=('Arial Bold', 14), bd=5)

    B3 = Button(menu, text="Exit", command=menu.quit, activeforeground='blue',
                activebackground="blue", bg="gray", fg="orange",
                width=500, height=5, font=('Arial Bold', 14), bd=5)
    head.pack(side='top')
    B1.pack(side='top')
    B2.pack(side='top')
    B3.pack(side='top')
    menu.mainloop()


# Call main function
if __name__ == '__main__':
    play()
