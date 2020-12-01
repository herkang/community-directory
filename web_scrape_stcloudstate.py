from bs4 import BeautifulSoup
import requests

import pandas as pd
import json
import csv
import crud

url = 'https://www.stcloudstate.edu/mrc/outreach/mn-orgs.aspx'

dfs = pd.read_html(url)

df = dfs[0]

df2 = df[['Category', 'Org Name', 'Contact', 'Address', 'Location']]

df2.to_csv('database.csv')

