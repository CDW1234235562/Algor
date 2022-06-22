from flask import Flask
import rhino3dm as rhino
import pandas as pd


sa2 = pd.read_csv('2016Census_P01_NSW_SA2.csv')

Tot_P_P = sa2['Tot_P_P']
SA2_MAINCODE = sa2['SA2_MAINCODE_2016']

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Link start!'


@app.route('/Tot_P_P/<sa2_code>')
def population(sa2_code):
    for sa2_code in SA2_MAINCODE:
        if (SA2_MAINCODE == sa2_code):
            total_population = sa2.iloc[sa2_code, [3]]
            return ('that is a NSW SA2 code!'+'population is' + total_population)

        else:
            return 'you type the wrong code!'
