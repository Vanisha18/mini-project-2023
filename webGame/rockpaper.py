from tkinter import *
from PIL import Image, ImageTk
from random import randint

window = Tk()
window.title("Game Rock Paper and Scissor")
bg = PhotoImage( file = "BG.png")
label1 = Label( window, image = bg)
label1.place(x = 0,y = 0)
  
image_rock1 = ImageTk.PhotoImage(Image.open("rock 1.png"))
image_paper1 = ImageTk.PhotoImage(Image.open("paper 1.png"))
image_scissor1 = ImageTk.PhotoImage(Image.open("scissor 1.png"))
image_rock2 = ImageTk.PhotoImage(Image.open("rock 2.png"))
image_paper2 = ImageTk.PhotoImage(Image.open("paper 2.png"))
image_scissor2 = ImageTk.PhotoImage(Image.open("scissor 2.png"))


label_player = Label(window,image=image_scissor1)
label_computer = Label(window,image=image_scissor2)
label_computer.grid(row=1,column=0,pady=50)
label_player.grid(row=1,column=4,pady=50)

computer_score = Label(window,text=0,font=("arial",40,"bold"),fg="red")
player_score = Label(window,text=0,font=("arial",40,"bold"),fg="red")
computer_score.grid(row=1,column=1)
player_score.grid(row=1,column=3)

player_indicator = Label(window,font=("arial",40,"bold"),
	                     text="PLAYER",bg="orange",fg="blue")
computer_indicator = Label(window,font=("arial",40,"bold"),
	                     text="COMPUTER",bg="orange",fg="blue")
computer_indicator.grid(row=0,column=0)	      	              
player_indicator.grid(row=0,column=4)

def updateMessage(a):
	final_message["text"]=a
	

def Computer_Update():
	final = int(computer_score["text"])
	final +=1
	computer_score["text"] = str(final)

def Player_Update():
	final = int(player_score["text"])
	final +=1
	player_score["text"] = str(final)

def winner_check(p,c):
        
	if p == c:
		updateMessage("It's a Tie")
	elif p == "rock":
		if c == "paper":
			updateMessage("Computer Wins !")
			Computer_Update()
		else:
			updateMessage("Player Wins !")
			Player_Update()

	elif p == "paper":
		if c == "scissor":
			updateMessage("Computer Wins !")
			Computer_Update()
		else:
			updateMessage("Player Wins !")
			Player_Update()

	elif p == "scissor":
		if c == "rock":
			updateMessage("Computer Wins !")
			Computer_Update()
		else:
			updateMessage("Player Wins !")
			Player_Update()

	else:
		pass

to_select = ["rock","paper","scissor"]

def choice_update(a):
	choice_computer = to_select[randint(0,2)]
	if choice_computer == "rock":
		label_computer.configure(image=image_rock2)
	elif choice_computer == "paper":
		label_computer.configure(image=image_paper2)
	else:
		label_computer.configure(image=image_scissor2)

	if a == "rock":
		label_player.configure(image=image_rock1)
	elif a == "paper":
		label_player.configure(image=image_paper1)
	else:
		label_player.configure(image=image_scissor1)

	winner_check(a,choice_computer)

def new_game():
        computer_score['text']=0
        player_score['text']=0
       

final_message = Label(window,font=("arial",30,"bold"),bg="yellow")
final_message.grid(row=0,column=2)

button_rock = Button(window,width=15,height=3,text="ROCK",
	                 font=("arial",20,"bold"),bg="yellow",fg="red",command=lambda:choice_update("rock")).grid(row=2,column=0)
button_paper = Button(window,width=15,height=3,text="PAPER",
	                 font=("arial",20,"bold"),bg="yellow",fg="red",command=lambda:choice_update("paper")).grid(row=2,column=2)
button_scissor = Button(window,width=15,height=3,text="SCISSOR",
	                 font=("arial",20,"bold"),bg="yellow",fg="red",command=lambda:choice_update("scissor")).grid(row=2,column=4)
reset_button=Button(window,width=32,height=2,text="restart",
	                 font=("arial",20,"bold"),bg="yellow",fg="red",command=lambda:new_game()).grid(row=4,column=2)

window.mainloop()
