from tkinter import *
import random 
from PIL import Image,ImageTk

#creating the window application
window = Tk()
window.title('Rock Paper Scissors')
window.geometry('621x760')
window.config(bg='gold')

#load the images as objects
Rock = Image.open('rock.png')
resized_rock = Rock.resize((150,150))
rock = ImageTk.PhotoImage(resized_rock)

Paper = Image.open('paper.png')
resized_paper = Paper.resize((150,150))
paper = ImageTk.PhotoImage(resized_paper)

Scissors = Image.open('scissors.png')
resized_scissors = Scissors.resize((150,150))
scissors = ImageTk.PhotoImage(resized_scissors)

choices = [rock,paper,scissors]

#Player and computer scores
P_Wins = 0
C_Wins = 0


#defining the function for the game 
def play(player_choice):
    global choices,P_Wins,C_Wins
    
    # update the labels with the image
    player.config(image=player_choice)
    
    #random choice from the computer
    computer_choice = random.choice(choices)
    computer.config(image=computer_choice)
    
    # The game logic
    #The game logic
    if (player_choice == computer_choice) :
        score.config(text=f"Draw\n Score: {P_Wins} for Player VS {C_Wins} for Computer",fg='blue')
    elif (player_choice == choices[0] and computer_choice == choices[2]) or \
         (player_choice == choices[1] and computer_choice == choices[0]) or \
         (player_choice == choices[2] and computer_choice == choices[1]):
        P_Wins +=1
        score.config(text=f'Player Wins\n Score: {P_Wins} for Player VS {C_Wins} for Computer',fg='green')
    else:
        C_Wins += 1
        score.config(text=f'Computer Wins\n Score: {C_Wins} for Computer VS {P_Wins} for Player',fg='red')


#creating the gui components
score = Label(window,text='Score',font=('Monospace',14,'italic'),bg='gold')
score.pack(pady=10)

# the computer and the player choices
computer = Label(window,image=rock,bg='gold')
computer.pack(pady=10)

player = Label(window,image=rock,bg='gold')
player.pack(pady=10) 

#frame that will contain the buttons
frame = Frame(window)
frame.config(bg='gold')
frame.pack()

# Adding buttons to the frame
rock_button = Button(frame,image=rock,bg='gold',command=lambda:play(choices[0]))
rock_button.grid(row=0,column=0,padx=20,pady=10)

paper_button = Button(frame,image=paper,bg='gold',command=lambda:play(choices[1]))
paper_button.grid(row=0,column=1,padx=20,pady=10)

scissors_button = Button(frame,image=scissors,bg='gold',command=lambda:play(choices[2]))
scissors_button.grid(row=0,column=2,padx=20,pady=10)
window.mainloop()
