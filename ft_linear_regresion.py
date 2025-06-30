import json
from price import initiate_prediction
from precision import calculate_precision
from train import launch_training
from train import  graphs

def initialize_thetas():
    with open('theta.json', 'w') as myJson:
        json.dump({"Theta0": 0, "Theta1": 0, "ThetaNorm0": 0, "ThetaNorm1": 0}, myJson)


def main():

    print("Welcome to...")
    print("\033[31mHOW \033[34mMUCH \033[35mIS \033[33mYOUR \033[32mCAR\033[0m??")
    while(True):
        inp=input("Please select what you want to do:\n1 - Predict your car's price 🤑\n2 - Train the Algorithm 🦾\n3 - Calculate Precision of the Algorithm 🎯\n4 - Clean Data 🧹\n5 - Graphs! 📈\n6 - Exit 🏃\n\nYour choice: ")
        try:
            inp = int(inp)
        except:
            print("That's not a number, Silly-Billy")
        match inp:
            case 1:
                initiate_prediction()
            case 2:
                print("Initiating Training Music... 🎶👁️🐅")
                launch_training()
                print("Bad Ass Training Done! 🦾🤖")
            case 3:
                print("Precision of the program: ")
                calculate_precision()
            case 4:
                print("Sweeping the floor... 🧹🧹🧹🧹🧹🧹🧹🧹🧹🧹🧹🧹🧹🧹🧹🧹")
                initialize_thetas()
                print("Cleaning Done! 👌")
            case 5:
                print("Please refer to your human companion for explanation! 🤓")
                graphs()
                print("WOW! I feel so Informed! 🧠")
            case 6:
                print("Bye Bye! 👋")
                break
            case _:
                print("Let's Try Again... 🤦")
        print("\n\033[32mStarting Again...\033[0m\n")
if __name__ == "__main__":
    main()