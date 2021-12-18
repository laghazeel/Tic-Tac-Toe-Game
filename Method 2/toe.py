# Tic Tac Toe game  programmed by Laghzal Mouad .


from tkinter import *
from tkinter import messagebox

root = Tk()
root.title('Laghazeel - Tic-Tac-Toe')




# disable all the buttons
def  disable_all_buttons():
	 btn1.config(state=DISABLED)
	 btn2.config(state=DISABLED)
	 btn3.config(state=DISABLED)
	 btn4.config(state=DISABLED)
	 btn5.config(state=DISABLED)
	 btn6.config(state=DISABLED)
	 btn7.config(state=DISABLED)
	 btn8.config(state=DISABLED)
	 btn9.config(state=DISABLED)



# check the winners 

def checkWon():
	global Winner
	Winner = False
	# chek for X

	if  btn1["text"] == "X" and btn2["text"] == "X" and btn3["text"] == "X":
		  btn1.config(bg="red")
		  btn2.config(bg="red")
		  btn3.config(bg="red")
		  Winner = True
		  messagebox.showinfo("Tic Tac Toe", "X wins !!")
		  disable_all_buttons()

	elif  btn4["text"] == "X" and btn5["text"] == "X" and btn6["text"] == "X":
		   btn4.config(bg="red")
		   btn5.config(bg="red")
		   btn6.config(bg="red")
		   Winner = True
		   messagebox.showinfo("Tic Tac Toe", "X wins !!")
		   disable_all_buttons()

	elif  btn4["text"] == "X" and btn5["text"] == "X" and btn6["text"] == "X":
		   btn4.config(bg="red")
		   btn5.config(bg="red")
		   btn6.config(bg="red")
		   Winner = True
		   messagebox.showinfo("Tic Tac Toe", "X wins !!")
		   disable_all_buttons()

	elif  btn7["text"] == "X" and btn8["text"] == "X" and btn9["text"] == "X":
		   btn7.config(bg="red")
		   btn8.config(bg="red")
		   btn9.config(bg="red")
		   Winner = True
		   messagebox.showinfo("Tic Tac Toe", "X wins !!")
		   disable_all_buttons()

	elif  btn1["text"] == "X" and btn4["text"] == "X" and btn7["text"] == "X":
		   btn1.config(bg="red")
		   btn4.config(bg="red")
		   btn7.config(bg="red")
		   Winner = True
		   messagebox.showinfo("Tic Tac Toe", "X wins !!")
		   disable_all_buttons()

	elif  btn2["text"] == "X" and btn5["text"] == "X" and btn8["text"] == "X":
		   btn2.config(bg="red")
		   btn5.config(bg="red")
		   btn8.config(bg="red")
		   Winner = True
		   messagebox.showinfo("Tic Tac Toe", "X wins !!")
		   disable_all_buttons()

	elif  btn3["text"] == "X" and btn6["text"] == "X" and btn9["text"] == "X":
		   btn3.config(bg="red")
		   btn6.config(bg="red")
		   btn9.config(bg="red")
		   Winner = True
		   messagebox.showinfo("Tic Tac Toe", "X wins !!")
		   disable_all_buttons()

	elif  btn1["text"] == "X" and btn5["text"] == "X" and btn9["text"] == "X":
		   btn1.config(bg="red")
		   btn5.config(bg="red")
		   btn9.config(bg="red")
		   Winner = True
		   messagebox.showinfo("Tic Tac Toe", "X wins !!")
		   disable_all_buttons()

	elif  btn3["text"] == "X" and btn5["text"] == "X" and btn7["text"] == "X":
		   btn3.config(bg="red")
		   btn5.config(bg="red")
		   btn7.config(bg="red")
		   Winner = True
		   messagebox.showinfo("Tic Tac Toe", "X wins !!")
		   disable_all_buttons()

	# chek for O
	elif  btn1["text"] == "O" and btn2["text"] == "O" and btn3["text"] == "O":
		   btn1.config(bg="red")
		   btn2.config(bg="red")
		   btn3.config(bg="red")
		   Winner = True
		   messagebox.showinfo("Tic Tac Toe", "O wins !!")
		   disable_all_buttons()

	elif  btn4["text"] == "O" and btn5["text"] == "O" and btn6["text"] == "O":
		   btn4.config(bg="red")
		   btn5.config(bg="red")
		   btn6.config(bg="red")
		   Winner = True
		   messagebox.showinfo("Tic Tac Toe", "O wins !!")
		   disable_all_buttons()

	elif  btn4["text"] == "O" and btn5["text"] == "O" and btn6["text"] == "O":
		   btn4.config(bg="red")
		   btn5.config(bg="red")
		   btn6.config(bg="red")
		   Winner = True
		   messagebox.showinfo("Tic Tac Toe", "O wins !!")
		   disable_all_buttons()

	elif  btn7["text"] == "O" and btn8["text"] == "O" and btn9["text"] == "O":
		   btn7.config(bg="red")
		   btn8.config(bg="red")
		   btn9.config(bg="red")
		   Winner = True
		   messagebox.showinfo("Tic Tac Toe", "O wins !!")
		   disable_all_buttons()

	elif  btn1["text"] == "O" and btn4["text"] == "O" and btn7["text"] == "O":
		   btn1.config(bg="red")
		   btn4.config(bg="red")
		   btn7.config(bg="red")
		   Winner = True
		   messagebox.showinfo("Tic Tac Toe", "O wins !!")
		   disable_all_buttons()

	elif  btn2["text"] == "O" and btn5["text"] == "O" and btn8["text"] == "O":
		   btn2.config(bg="red")
		   btn5.config(bg="red")
		   btn8.config(bg="red")
		   Winner = True
		   messagebox.showinfo("Tic Tac Toe", "O wins !!")
		   disable_all_buttons()

	elif  btn3["text"] == "O" and btn6["text"] == "O" and btn9["text"] == "O":
		   btn3.config(bg="red")
		   btn6.config(bg="red")
		   btn9.config(bg="red")
		   Winner = True
		   messagebox.showinfo("Tic Tac Toe", "O wins !!")
		   disable_all_buttons()

	elif  btn1["text"] == "O" and btn5["text"] == "O" and btn9["text"] == "O":
		   btn1.config(bg="red")
		   btn5.config(bg="red")
		   btn9.config(bg="red")
		   Winner = True
		   messagebox.showinfo("Tic Tac Toe", "O wins !!")
		   disable_all_buttons()

	elif  btn3["text"] == "O" and btn5["text"] == "O" and btn7["text"] == "O":
		   btn3.config(bg="red")
		   btn5.config(bg="red")
		   btn7.config(bg="red")
		   Winner = True
		   messagebox.showinfo("Tic Tac Toe", "O wins !!")
		   disable_all_buttons()

	# check if there is a tie 
	if count == 9 and Winner == False:
		messagebox.showinfo("Tic Tac Toe", "It's a Tie")
		disable_all_buttons() 	   

# who start the game 
clicked = True
count = 0

def btn_click(btn):
	global clicked, count

	if btn["text"] == " " and clicked == True:
		btn["text"] = "X"
		clicked = False
		count += 1 
		checkWon()
	elif btn["text"] == " " and clicked == False:
		btn["text"] = "O"
		clicked = True
		count +=1
		checkWon()
	else:
		messagebox.showerror("Tic Tac Toe", "Sorry ! the box already selected\nChoose Another One ")

# reset the game 
def reset():
	global btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9
	global clicked, count
	clicked = True
	count = 0

	# Build buttons 
	btn1 = Button(root, text=" ", font=("boldface", 20), height=5, width= 10, bg="SystemButtonFace", command=lambda: btn_click(btn1))
	btn2 = Button(root, text=" ", font=("boldface", 20), height=5, width= 10, bg="SystemButtonFace", command=lambda: btn_click(btn2))
	btn3 = Button(root, text=" ", font=("boldface", 20), height=5, width= 10, bg="SystemButtonFace", command=lambda: btn_click(btn3))

	btn4 = Button(root, text=" ", font=("boldface", 20), height=5, width= 10, bg="SystemButtonFace", command=lambda: btn_click(btn4))
	btn5 = Button(root, text=" ", font=("boldface", 20), height=5, width= 10, bg="SystemButtonFace", command=lambda: btn_click(btn5))
	btn6 = Button(root, text=" ", font=("boldface", 20), height=5, width= 10, bg="SystemButtonFace", command=lambda: btn_click(btn6))

	btn7 = Button(root, text=" ", font=("boldface", 20), height=5, width= 10, bg="SystemButtonFace", command=lambda: btn_click(btn7))
	btn8 = Button(root, text=" ", font=("boldface", 20), height=5, width= 10, bg="SystemButtonFace", command=lambda: btn_click(btn8))
	btn9 = Button(root, text=" ", font=("boldface", 20), height=5, width= 10, bg="SystemButtonFace", command=lambda: btn_click(btn9))

	# display the buttons with Grid
	btn1.grid(row=0, column=0) 
	btn2.grid(row=0, column=1)
	btn3.grid(row=0, column=2)

	btn4.grid(row=1, column=0)
	btn5.grid(row=1, column=1)
	btn6.grid(row=1, column=2)

	btn7.grid(row=2, column=0)
	btn8.grid(row=2, column=1)
	btn9.grid(row=2, column=2)

	


# create menu 
my_menu = Menu(root)
root.config(menu=my_menu)

#menu options
options_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="Options", menu=options_menu) 
options_menu.add_command(label="Rest Game", command=reset)
reset()

root.mainloop()