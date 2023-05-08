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
df.plot(x = "Language", y = "Percentage of world population (2022)")

plt.show()