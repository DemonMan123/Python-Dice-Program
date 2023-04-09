import time
import pyfiglet
import os

Health = 20

def Main():
    time.sleep(1)
    os.system('cls' if os.name=='nt' else 'clear')
    
    global Health
    
    HealthFormatted = pyfiglet.figlet_format(str(f"Health {Health}"))
    
    print(HealthFormatted)
    time.sleep(1)
    try:
        HealthVal = int(input("\nEnter number to add/subtract to health: "))
        print("\nPress 'enter' to view your current health or 'e' to exit the program")
        Op = input("\nAre you adding or subtracting? (+, -) ")
    
        if Op == "+":
            Health += HealthVal
        elif Op == "-":
            Health -= HealthVal
        elif Op == "e":
            exit()
        else:
            print(f"Your current helth: {Health}")
    except ValueError:
        print("Something went wrong...")
    
while True:
    if Health <= 0:
        print("\nYou're dead..")
        print("Exiting...")
        time.sleep(2)
        exit()
    Main()