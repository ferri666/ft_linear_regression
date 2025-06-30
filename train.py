import pandas as pd
import json
import matplotlib.pyplot as plt
from price import estimatePrice

def normalize(series):
    min_val = series.min()
    max_val = series.max()
    normalized_data = (series - min_val) / (max_val - min_val)
    return normalized_data

def denormalize(df, t0, t1):
    
    minPrice_val = df['price'].min()
    maxPrice_val = df['price'].max()
    minKm_val = df['km'].min()
    maxKm_val = df['km'].max()
    
    t0_denorm = 0
    t1_denorm = 0
    
    t0_denorm = t0 * (maxPrice_val - minPrice_val) + minPrice_val +\
    (t1 * minKm_val * (minPrice_val - maxPrice_val)) / (maxKm_val - minKm_val)
    t1_denorm = t1 * (maxPrice_val - minPrice_val) / (maxKm_val - minKm_val)
    
    return t0_denorm, t1_denorm

def train(df, t0, t1):
    learningRate = 0.6
    sumErrorT0 = 0
    sumErrorT1 = 0
    for index, car in df.iterrows():
        price = car['price']
        km = car['km']
        prediction = estimatePrice(km, t0, t1)
        error = prediction - price
        sumErrorT0 += error
        sumErrorT1 += error * km
    t0 -= learningRate * 1 / len(df) * sumErrorT0
    t1 -= learningRate * 1 / len(df) * sumErrorT1
    return (t0, t1)

def launch_training():

    t0, t1 = 0,0

    df = pd.read_csv('data.csv')
    normalized_data = {}
    normalized_data['price'] = normalize(df['price'])
    normalized_data['km'] = normalize(df['km'])
    df_normalized = pd.DataFrame(normalized_data)
    while (True):
            oldT0 = t0
            oldT1 = t1
            t0, t1 = train(df_normalized, t0, t1)

            if (t0 == oldT0 and t1 == oldT1):
                break
    rt0, rt1 = denormalize(df, t0, t1)
    price0 = estimatePrice(df['km'].min(), rt0, rt1)
    price1 = estimatePrice(df['km'].max(), rt0, rt1)
    with open('theta.json', 'w') as myJson:
            json.dump({"Theta0": rt0, "Theta1": rt1, "ThetaNorm0": t0, "ThetaNorm1": t1}, myJson)

def graphs():
    t0, t1 = 0,0
    df = pd.read_csv('data.csv')
    normalized_data = {}
    normalized_data['price'] = normalize(df['price'])
    normalized_data['km'] = normalize(df['km'])
    df_normalized = pd.DataFrame(normalized_data)
    while (True):
            oldT0 = t0
            oldT1 = t1
            t0, t1 = train(df_normalized, t0, t1)
            price0 = estimatePrice(0, t0, t1)
            price1 = estimatePrice(1, t0, t1)
            plt.xlabel('Kilometers')
            plt.ylabel('Price')
            plt.title('Training')
            plt.plot([0,1], [price0,price1], color='red')
            if (t0 == oldT0 and t1 == oldT1):
                break
    plt.show()
    rt0, rt1 = denormalize(df, t0, t1)
    price0 = estimatePrice(df['km'].min(), rt0, rt1)
    price1 = estimatePrice(df['km'].max(), rt0, rt1)
    plt.scatter(df['km'], df['price'])
    plt.xlabel('Kilometers')
    plt.ylabel('Price')
    plt.title('Price vs Kilometers')
    plt.plot([df['km'].min(),df['km'].max()], [price0,price1], color='red')
    plt.show()

def main():

    t0, t1 = 0,0

    df = pd.read_csv('data.csv')
    normalized_data = {}
    normalized_data['price'] = normalize(df['price'])
    normalized_data['km'] = normalize(df['km'])
    df_normalized = pd.DataFrame(normalized_data)
    plt.scatter(df['km'], df['price'])
    plt.xlabel('Kilometers')
    plt.ylabel('Price')
    plt.title('Price vs Kilometers')

    while (True):
            oldT0 = t0
            oldT1 = t1
            t0, t1 = train(df_normalized, t0, t1)

            if (t0 == oldT0 and t1 == oldT1):
                break
    rt0, rt1 = denormalize(df, t0, t1)
    price0 = estimatePrice(df['km'].min(), rt0, rt1)
    price1 = estimatePrice(df['km'].max(), rt0, rt1)
    plt.plot([df['km'].min(),df['km'].max()], [price0,price1], color='red')


    with open('theta.json', 'w') as myJson:
            json.dump({"Theta0": rt0, "Theta1": rt1, "ThetaNorm0": t0, "ThetaNorm1": t1}, myJson)
    plt.show()

if __name__ == "__main__":
    main()