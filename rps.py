from tkinter import *
import random

root = Tk()
root.title('Rock, Paper, Scissors')


#Variables & Dict ===========
events = {
    'rock':{'rock':None,'paper':0,'scissors':1},
    'paper':{'rock':1,'paper':None,'scissors':0},
    'scissors':{'rock':0,'paper':1,'scissors':None}
}


font_cal14 = ('Calibri', 14)
player_score = 0
comp_score = 0


# Funtion
def outcome_handler(user_choice):
    global player_score
    global comp_score

    outcomes = ['rock','paper','scissors']
    rand_num = random.randint(0,2)
    comp_choice = outcomes[rand_num]

    result = events[user_choice][comp_choice]

    player_choice_lbl.config(fg='red', text='Player : '+str(user_choice))
    comp_choice_lbl.config(fg='green', text='Computer : '+str(comp_choice))
    
    if result == 1:
        player_score+=1
        player_score_lbl.config( text='Player : '+str(player_score))
        outcome_lbl.config(fg='blue', text='Outcome: Player Won!')

    elif result == 0:
        comp_score+=1
        comp_score_lbl.config( text='Computer : '+str(comp_score))
        outcome_lbl.config(fg='blue', text='Outcome: Computer Won!')


    else:
        outcome_lbl.config(fg='blue', text='Outcome: Draw!')


    



# Labels ============
Label(root, text='Rock, Paper, Scissors', font=('Calibri', 20, 'bold')).grid(row=0, sticky=N,pady=10,padx=150)
Label(root, text='Please select an option', font=('Calibri', 16)).grid(row=1, sticky=N)
#Score 
player_score_lbl = Label(root, text="Player : 0", font=font_cal14 )
player_score_lbl.grid(row=2, sticky=W,padx=5)

comp_score_lbl = Label(root, text="Computer : 0", font=font_cal14 )
comp_score_lbl.grid(row=2, sticky=E,padx=5)
#Choice
player_choice_lbl = Label(root, font=font_cal14)
player_choice_lbl.grid(row=3,sticky=W,padx=5)

comp_choice_lbl = Label(root, font=font_cal14)
comp_choice_lbl.grid(row=3,sticky=E,padx=5)

outcome_lbl = Label(root, font=font_cal14)
outcome_lbl.grid(row=3,sticky=N)


#Buttons
Button(root, text="Rock", width=15, command=lambda: outcome_handler('rock')).grid(row=4,sticky=W,padx=5,pady=10)
Button(root, text="Paper", width=15, command=lambda: outcome_handler('paper')).grid(row=4,sticky=N,padx=5,pady=10)
Button(root, text="Scissors", width=15, command=lambda: outcome_handler('scissors')).grid(row=4,sticky=E,padx=5,pady=10)


#Dummy lbl
Label(root).grid(row=5)



root.mainloop()
