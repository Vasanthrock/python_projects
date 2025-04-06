import csv
import pandas as pd
from numpy.ma.extras import average
from numpy.testing.print_coercion_tables import print_new_cast_table

# with open("./weather_data.csv", "r") as file:
#    store =  csv.reader(file)
#    temperatures = []
#    for row in store:
#     temperatures.append(row[1])
# print(temperatures)
# df=pd.read_csv("./weather_data.csv")
# series=df["temp"]
# print(average(series))
# series1=df[df.day=="Monday"]
# print(series1.temp)
df = pd.read_csv("./Squirrel-Data.csv")
red = len(df[df["Primary Fur Color"] == "Cinnamon"])
black = len(df[df["Primary Fur Color"] == "Black"])
gray = len(df[df["Primary Fur Color"] == "Gray"])

dict= {
    "Fur_color" : ["Cinnamon","Black","Gray"],
    "count": [red,black,gray]

}
data = pd.DataFrame(dict)
data.set_index("Fur_color",inplace=True)
data.to_csv("sample.csv")

