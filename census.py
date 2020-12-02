import pandas as pd
import csv

url = 'https://www.census.gov/quickfacts/fact/table/MN,US/POP010210#POP010210'

dataframe = pd.read_html(url)

people = dataframe[1]

print(people)