from flask import Flask
import rhino3dm as rhino
import pandas as pd
import ghhops_server as hs

filepath = '/home/cdw1234235562/Algor/2016Census_P01_NSW_SA2.csv'
sa2 = pd.read_csv(filepath)

Tot_P_P = sa2['Tot_P_P']
SA2_MAINCODE = sa2['SA2_MAINCODE_2016'].tolist()

app = Flask(__name__)
hops = hs.Hops(app)


@app.route('/')
def hello_world():
    return 'Link start!'


@hops.component(
    "/hops_sa2_population",
    name="sa2_population",
    description="Get sa2 block population",
    inputs=[
        hs.HopsNumber("Sa2_code", "Sa2_code", "sa2 main code 2016ver."),
        ],
    outputs=[
        hs.HopsNumber("Total_population", "Tot_P", "Total population on this SA2 block")
    ]
)
def sa2_population(Sa2_code):
    if Sa2_code in SA2_MAINCODE:
        index = sa2[sa2["SA2_MAINCODE_2016"] == Sa2_code].index.tolist()[0]
        population = int(sa2.iloc[index, [3]])
    return population


if __name__ == "__main__":
    app.run()
