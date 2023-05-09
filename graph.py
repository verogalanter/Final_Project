import bs4
import pandas as pd
import requests
import matplotlib.pyplot as plt

#gets the website and table information
tables = pd.read_html(
    "https://en.wikipedia.org/wiki/List_of_languages_by_total_number_of_speakers",
    match = "Most-spoken languages, CIA, 2022"

)

table = tables[0]
#sets up table
df = table[["Language", "Percentage of world population (2022)"]]
#prints out the percent info
print (df.info())
#makes percent recognized as a numerical value for printing
df["Percent"]=df["Percentage of world population (2022)"].str.extract('(\d+)').astype(int)
#prints out percent as numerical value
print (df.info())
#Sets up bar graph with x and y axis
df.plot.bar(x = "Language", y = "Percent")
#makes sure all ten languages are printing out
plt.xticks(range(0, 10), ['English', 'Mandarin Chinese', 'Hindi', 'Spanish', 'French', 'Arabic', 'Bengali', 'Russian', 'Portuguese', 'Urdu'])
#prints out final graph
plt.show()