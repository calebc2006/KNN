# list of lists of [AP1, AP2, x, y]
from KNN_data import Test_data, Train_data
import numpy as np
import math
import pandas as pd
import matplotlib.pyplot as plt
from statistics import stdev
NUM_AP = 2
ORDER = 2


def euclidean_distance(p1, p2):
    distance = 0.0
    for i in range(NUM_AP):
        distance += (p1[i] - p2[i])**2
    return math.sqrt(distance)


def get_neighbors(train, test_row, num_neighbors):
    distances = list()
    for train_row in train:
        dist = euclidean_distance(test_row, train_row)
        distances.append((train_row, dist))
    distances.sort(key=lambda tup: tup[1])
    neighbors = list()
    for i in range(num_neighbors):
        neighbors.append(distances[i][0])
    return neighbors


def get_prediction(test_case, k):
    neighbors = get_neighbors(Train_data, test_case, k)

    x_pred = 0
    y_pred = 0
    total = 0
    inverse_dev = []

    for i in range(k):
        dist = euclidean_distance(test_case, neighbors[i][0:NUM_AP])
        if dist == 0:
            inverse_dev.append(1e9)
        else:
            inverse_dev.append(float(1/dist**ORDER))
        total += inverse_dev[i]
    for i in range(k):
        inverse_dev[i] /= total
        x_pred += neighbors[i][NUM_AP] * inverse_dev[i]
        y_pred += neighbors[i][NUM_AP+1] * inverse_dev[i]
    return [x_pred, y_pred]


def evaluate_model(k):
    max_dev = 0
    min_dev = 1e9
    total_dev = 0
    num_testcases = 0
    a = []
    for i in Test_data:
        arr = i[0:NUM_AP]
        x_ans = i[NUM_AP]
        y_ans = i[NUM_AP+1]
        prediction = get_prediction(arr, k)
        deviation = round(
            math.sqrt((prediction[0]-x_ans)**2 + (prediction[1]-y_ans)**2), 2)
        max_dev = max(max_dev, deviation)
        min_dev = min(min_dev, deviation)
        total_dev += deviation
        num_testcases += 1
        a.append(deviation)
    return [round(total_dev/num_testcases, 2), max_dev, min_dev, a]


def run_eval():
    Average_deviation = [0]
    Maximum_deviation = [0]
    Minimum_deviation = [0]
    raw_data = []

    for k in range(1, 20):
        data = evaluate_model(k)
        Average_deviation.append(data[0])
        Maximum_deviation.append(data[1])
        Minimum_deviation.append(data[2])
        raw_data.append([k, data[0], round(stdev(data[3]), 2)])

    df = pd.DataFrame(raw_data, columns=[
                      "K", "Average Error (m)", "Standard Deviation"])
    print(df.to_string(index=False))
    df.to_csv('KNNerrors.csv', index=False)


def main():
    run_eval()  # Varies the value of k in the algorithm to find optimal value (pick the best k)


if __name__ == "__main__":
    main()
