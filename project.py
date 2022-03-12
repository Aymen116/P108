import csv
import imp
import plotly.express as pl
import pandas as pa
import plotly.figure_factory as plf
df = pa.read_csv("project.csv")
figure = plf.create_distplot([df["Avg Rating"].tolist()],["AvgRating"])
figure.show()