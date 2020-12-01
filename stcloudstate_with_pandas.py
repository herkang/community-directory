import pandas as pd
import csv

url = 'https://www.stcloudstate.edu/mrc/outreach/mn-orgs.aspx'

dataframe = pd.read_html(url)[0]

dataframe_without_missing_columns = dataframe.dropna()

dataframe_without_missing_columns.to_csv('database.cvs')