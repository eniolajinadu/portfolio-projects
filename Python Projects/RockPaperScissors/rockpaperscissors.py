##ROCKPAPERSCISSORS!
print ("ROCKPAPERSCISSORS!")
import random
b = 0
c = 1
computer = random.choice(["rock", "paper", "scissors"])

while b < c:
    b += 1
    user = input("Enter your choice: ").lower()
    if user not in ["rock", "paper", "scissors"]:
        print ("Incorrect input, input rock, paper or scissors")
        user = input("Enter your choice: ").lower()
        

    
if user == computer:
    print ("It's a tie")
elif (user == "rock" and computer == "scissors") or (user == "scissors" and computer == "paper") or (user == "paper" and computer == "rock"):
    print ("YOU WIN!")
else:
    print("YOU LOSE!")

print(f'{user}')
print(f'{computer}')