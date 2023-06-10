from flask import Flask
import numpy as np
from flask_cors import CORS
import json
import pandas as pd

app = Flask(__name__)
CORS(app)

df = pd.read_csv("data.csv")

@app.route('/')
def main():
    labels = ["January", "February", "March", "April", "May", "June"]
    l = {
        'labels': labels,
        'datasets': [
            {
                'label': "My First dataset",
                'backgroundColor': "rgb(255, 99, 132)",
                'borderColor': "rgb(255, 99, 132)",
                'data': [50, 5, 2, 7, 30, 20, 45],
            },
        ],
    }
    res = json.dumps(l)
    return res

@app.route('/test')
def test():
    global df

    local = "Europe"
    standardYear = 1990
    tempDf = df[df['category'] == local]
    transposeDf = tempDf.transpose()
    tempList = transposeDf.values.tolist()
    resList = []
    for item in tempList:
        resList.append(item[0])
    resList = resList[1:-2]
    x = list(range(len(resList)))
    for i in range(len(x)):
        x[i] += standardYear
    y = resList

    res = json.dumps({
        'labels': x,
        'datasets': [
            {
                'label': "My First dataset",
                'backgroundColor': "rgb(216, 90, 232)",
                'borderColor': "rgb(216, 90, 232)",
                'data': y,
            },
        ], 
    })
    return res

if __name__ == '__main__':
    app.run()
