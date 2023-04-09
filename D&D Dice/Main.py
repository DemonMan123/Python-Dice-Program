from D90 import D90Roll
from D20 import D20Roll
from D12 import D12Roll
from D9 import D9Roll
from D8 import D8Roll
from D6 import D6Roll
from D4 import D4Roll
import pyfiglet
import os

Title = pyfiglet.figlet_format("Demin's dice")

def main():
    input("Press any key to continue... ")
    os.system('cls' if os.name=='nt' else 'clear')
    print(Title)
    print("Roll types: ")
    print("A = Advantage")
    print("D = Disadvantage")
    print("N = Normal (D20 roll)")
    print("E to Exit\n")
    RollType = input("What type of roll would you like to do? ")
    if RollType.lower() == "a":
        AdvantageRoll()
    if RollType.lower() == "d":
        DisadvantageRoll()
    if RollType.lower() == "n":
        Roll = D20Roll()
        print("You rolled... ", Roll)
    if RollType.lower() == "e":
        exit()
        
        
def DisadvantageRoll():
    D12R = D12Roll()
    D20R = D20Roll()
    print("Values: ")
    print("D20: ", D20R)
    print("D12: ", D12R)
    if D12R < D20R:
        print("D12 is lower...")
    if D20R < D12R:
        print("D20 is lower...")
    else:
        print("Even")


def AdvantageRoll():
    D20R = D20Roll()
    D90R = D90Roll()
    print("Values: ")
    print("D20: ", D20R)
    print("D90: ", D90R)
    if D20R < D90R:
        print("D90 is higher")
    if D20R > D90R:
        print("D20 is higher")
    else:
        print("Even")

while True:
    main()