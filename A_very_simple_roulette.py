import random
from random import shuffle
import sys


numco=(["red",1],["black",2],["red",3],["black",4],["red",5],["black",6],["red",7],["black",8],["red",9],["black",10],["black",11],["red",12],
       ["black",13],["red",14],["black",15],["red",16],["black",17],["red",18],["red",19],["black",20],["red",21],["black",22],["red",23],
       ["black",24],["red",25],["black",26],["red",27],["black",28],["black",29],["red",30],["black",31],["red",32],["black",33],["red",34],
       ["black",35],["red",36],["green",0])
game= True
balance = 1000.0
bet = 0.0
d=""
c=""
num_guess = 0


def game_quit():
    gamequit = input("Press 'q' to quit the game,otherwise press any other key: ")
    if gamequit.lower() == "q":
        sys.exit()
       
        

def ask_for_bet():
    global balance
    global bet 
    bet = float(input("Set your bet amount:"))
    while  bet > balance:
        print("Insufficient balance")
        bet = float(input("Set your bet amount:"))
    balance -= bet

def bet_win():
    global balance
    global bet
    balance += bet*2
    print(f"Your current balance: {balance}")
    
def bet_loss():
    global balance
    global bet
    print(f"Your current balance: {balance}")
    
def bet_win_both():
    global balance
    global bet
    balance += bet*4
    
def half_win():
    global balance
    global bet
    balance += bet/2
def green_win():
    global balance
    global bet
    balance += bet*10
        
def bet_type():
    global d
    while d.lower()!= "color" or d.lower()!="both" or d.lower() != "number":
        d=input("Type 'color' to bet on a color \n 'number' for a number \n 'both' to bet on both: ")
        if d.lower() == "color" or d.lower()=="both" or d.lower()=="number":
            return d
            break
        
def color_bet_type():
    global c
    while c.lower()!= "green" or c.lower()!= "red" or c.lower()!= "black":
        c = input("Choose color to bet on: Red, Black or Green? : ")
        if c.lower()=="green" or c.lower()=="red" or c.lower()=="black":
            return c
            break
        
def num_bet_type():
    global num_guess
    num_guess = input("Type the number you want to bet on(0-36): ")
    while num_guess.isdigit()==False:
        num_guess = input("Type the number you want to bet on (0-36)!!: ")
        if num_guess.isdigit()==True:
            int(num_guess)
            return num_guess
    
    
def game_on():
    while game == True:
        print(f"\nYour current balance is: {balance}")
        ask_for_bet()
        bet_type()
        if d.lower() =="color":
            b = random.choice(numco)
            color_bet_type()
            print("Result was : ")
            print(b[0])
            if "red" in b:
                if c.lower()=="red":
                    print("Pays!!")
                    bet_win()
                    game_quit()
                elif c.lower()=="black":
                    print("You've lost!")
                    bet_loss()
                    game_quit()
                elif c.lower()=="green":
                    print("You've lost")
                    bet_loss()
                    game_quit()
            if "black" in b:
                if c.lower() == "black":
                    print("Pays!!")
                    bet_win()
                    game_quit()
                elif c.lower()== "red":
                    print("You've lost")
                    bet_loss()
                    game_quit()
                elif c.lower()=="green":
                    print("You've lost")
                    bet_loss()
                    game_quit()
            if "green" in b:
                if c.lower()=="green":
                    print("Pays!!")
                    green_win()
                    game_quit()
                elif c.lower()=="red":
                    print("You've lost")
                    bet_loss()
                    game_quit()
                elif c.lower()=="black":
                    print("You've lost")
                    bet_loss()
                    game_quit()
        if d.lower() == "number":
                num_guess=0
                g = random.choice(numco)
                num_bet_type()
                while num_guess > 36 or num_guess < 0:
                    num_guess = int(input("Only 0 to 36: "))
                    continue
                print(f"Number was : {g[1]}")
                if num_guess in g:
                    print("Pays!!")
                    bet_win()
                    game_quit()
                else:
                    print("Oops...better luck next time!")
                    bet_loss()
                    game_quit()
        if d.lower()=="both":
                num_guess=0
                x = random.choice(numco)
                color_bet_type()
                num_bet_type()
                while num_guess > 36 or num_guess < 0:
                    num_guess = int(input("Only 0 to 36: "))
                    continue
                print("Result was:")
                print(*x,sep="  ")
                if c.lower() in x and num_guess in x:
                    print("Congratulations!! Both bets pay!!")
                    bet_win_both()
                    game_quit()
                if "green" in x and 0 in x:
                    if c.lower() =="green" and num_guess == 0:
                        print("Congratulations!! Both bets pay")
                        green_win()
                        game_quit()
                if c.lower() not in x and num_guess not in x:
                    print("You've lost")
                    bet_loss()
                    game_quit()
                if c.lower() in x: 
                    print("Only color bet pays!")
                    half_win()
                    game_quit()
                elif num_guess in x:
                    print("Only number bet pays!")
                    half_win()
                    game_quit()
                
game_on()
           