import random
computer=random.choice(["r","p","s"])

dict={"r":"rock",
          "p":"paper",
          "s":"scissor"}
you=input("Enter your choice (s for scissor, p for paper and r for rock):")
print(f"You chose {dict[you]} and computer choose {dict[computer]}")

if (you=="s" and computer=="p") or (you=="p" and computer=="r") or  ( you=="r" and computer=="s"):
        print("You win")
elif computer==you:
        print("Both choose same no one wins")
else:
        print("computer wins")
    
