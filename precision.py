import pandas as pd
import json
from price import estimatePrice
import math

def calculate_precision():
    df = pd.read_csv('data.csv')
    with open("theta.json", "r") as myJson:
        myData = json.load(myJson)
    diff = 0
    diff_sq = 0
    t0 = myData['Theta0']
    t1 = myData['Theta1']
    for index, car in df.iterrows():
        price = car['price']
        km = car['km']
        prediction = estimatePrice(km, t0, t1)
        diff += abs(price - prediction)
        diff_sq += (price - prediction) * (price - prediction)
    mean_absolute_error = diff/len(df)
    mean_square_error = diff_sq/len(df)
    root_mean_square_error = math.sqrt(mean_square_error)
    print("Mean Absolute Error: +-", mean_absolute_error, "$")
    print("Mean Square Error:", mean_square_error)
    print("Root Mean Square Error: +-", root_mean_square_error, "$")


def main():
    calculate_precision()

if __name__ == "__main__":
    main()