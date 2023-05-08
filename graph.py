import bs4
import pandas as pd
import requests
import matplotlib.pyplot as plt

tables = pd.read_html(
    "https://en.wikipedia.org/wiki/List_of_languages_by_total_number_of_speakers",
    match = "Most-spoken languages, CIA, 2022"

)

table = tables[0]
df = table[["Language", "Percentage of world population (2022)"]]
print (df.info())
df["Percent"]=df["Percentage of world population (2022)"].str.extract('(\d+)').astype(int)
print (df.info())
df.plot(x = "Language", y = "Percent")

plt.show()