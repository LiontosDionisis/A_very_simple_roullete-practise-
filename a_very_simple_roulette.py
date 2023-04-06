import random
from random import shuffle
# d is to choose bet type
## c is to choose color in color bet 

nums =[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29
       ,30,31,32,33,34,35,36]
color=["red","black"]
numco=(["red",1],["black",2],["red",3],["black",4],["red",5],["black",6],["red",7],["black",8],["red",9],["black",10],["black",11],["red",12],
       ["black",13],["red",14],["black",15],["red",16],["black",17],["red",18],["red",19],["black",20],["red",21],["black",22],["red",23],
       ["black",24],["red",25],["black",26],["red",27],["black",28],["black",29],["red",30],["black",31],["red",32],["black",33],["red",34],
       ["black",35],["red",36])
game= True


def game_on():
    while game is True:
        d = input("What would you like to bet to? Type 'color' to bet on color, \n 'number' to bet on a number \n or 'both' to bet for a number and a color: ") 
        if d.lower() =="color":
            shuffle(color)
            c = input("Choose color to bet on: Red or Black? : ")
            print("Color was : ")
            print(color[0].upper())
            if color[0] == "red":
                if c.lower()=="red":
                    print("You've won!")
                elif c.lower()=="black":
                    print("You've lost!")
            if color[0]=="black":
                if c.lower() == "black":
                    print("You've won")
                elif c.lower()== "red":
                    print("You've lost")
        if d.lower() == "number":
                shuffle(nums)
                num_guess = int(input("Type the number you want to bet on(0-36): "))
                while num_guess > 36 or num_guess < 0:
                    num_guess = int(input("I said 0-36 smartass: "))
                    continue
                print(f"Number was : {nums[0]}")
                if nums[0]== num_guess:
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
                    print("Congratulations!! You've got both color and number")
                elif color_guess in x:
                    print("You've won...didn't find the number though")
                
                elif guess_num in x:
                    print("Nice!! You've found the number but missed the color")
                
game_on()
            
            
        
        