import pandas as pd
import csv
import plotly.figure_factory as ff

data1 = pd.read_csv("holymoly.csv")
figure = ff.create_distplot([data1["Avg Rating"].tolist()], ["Avg Rating"])
figure.show()