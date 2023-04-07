import random
from random import shuffle
import os

numco=(["red",1],["black",2],["red",3],["black",4],["red",5],["black",6],["red",7],["black",8],["red",9],["black",10],["black",11],["red",12],
       ["black",13],["red",14],["black",15],["red",16],["black",17],["red",18],["red",19],["black",20],["red",21],["black",22],["red",23],
       ["black",24],["red",25],["black",26],["red",27],["black",28],["black",29],["red",30],["black",31],["red",32],["black",33],["red",34],
       ["black",35],["red",36])
game= True


def clear():
    os.system('cls' if os.name=='nt' else 'clear')


def game_on():
    while game is True:
        d = input("What would you like to bet to? Type 'color' to bet on color, \n 'number' to bet on a number \n or 'both' to bet for a number and a color: ") 
        if d.lower() =="color":
            b = random.choice(numco)
            c = input("Choose color to bet on: Red or Black? : ")
            print("Result was : ")
            print(b[0])
            if "red" in b:
                if c.lower()=="red":
                    print("You've won!")
                elif c.lower()=="black":
                    print("You've lost!")
            if "black" in b:
                if c.lower() == "black":
                    print("You've won")
                elif c.lower()== "red":
                    print("You've lost")
        if d.lower() == "number":
                g = random.choice(numco)
                num_guess = int(input("Type the number you want to bet on(0-36): "))
                while num_guess > 36 or num_guess < 0:
                    num_guess = int(input("I said 0-36 smartass: "))
                    continue
                print(f"Number was : {g[1]}")
                if num_guess in g:
                    print("Wow...You've won")
                else:
                    print("Oops...better luck next time!")
        if d.lower()=="both":
                x = random.choice(numco)
                color_guess = input("Choose color to bet on: Red or Black? : ")
                guess_num = int(input("Choose a number(0-36):  "))
                while guess_num > 36 or guess_num < 0:
                    guess_num = int(input("I said 0-36 :D : "))
                    continue
                print("Result was :")
                print(*x,sep="  ")
                if color_guess in x and guess_num in x:
                    print("Congratulations!! Both bets pay!!")
                if color_guess not in x and guess_num not in x:
                    print("You've lost")
                if color_guess in x: 
                    print("Color bet pays!")
                
                elif guess_num in x:
                    print("Number bet pays!")
                
game_on()
            
            
        
        