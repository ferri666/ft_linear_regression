import json

def estimatePrice(mileage, theta0, theta1):
    estPrice=float(theta0) + (float(theta1) * float(mileage))
    return (estPrice)

def initiate_prediction():
    with open("theta.json", "r") as myJson:
        myData = json.load(myJson)
        
    mileage = "start"
    while (mileage.isdigit() == False):
        mileage = input("Please, Insert the mileage of your car: ")

    mileage = float(mileage)
    estimateCarPrice = estimatePrice(mileage, myData["Theta0"], myData["Theta1"])

    print("Estimated Price: ", estimateCarPrice, "$")
    if (mileage == 0):
        print("Brand new and you want to get rid of it!? 🚗")
    elif (estimateCarPrice < 0):
        print("Who would want that piece of trash??? 🤢")
    elif (estimateCarPrice == 0):
        print("Oops! Did you forgot to train the Algorithm? 🫤")
    else:
        print("WOW!! That's a Bargain!!! 🤑")
def main():
    with open("theta.json", "r") as myJson:
        myData = json.load(myJson)
        
    mileage = "start"
    while (mileage.isdigit() == False):
        mileage = input("Please, Insert the mileage of your car: ")

    mileage = float(mileage)
    estimateCarPrice = estimatePrice(mileage, myData["Theta0"], myData["Theta1"])

    print("Estimated Price: ", estimateCarPrice, "$")


if __name__ == "__main__":
    main()