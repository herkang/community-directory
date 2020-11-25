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

df2.to_csv('db.csv')

with open('db.csv', 'r') as data:

    for line in csv.DictReader(data):
        for k, v in line.items():
            # print({k: v})
            # print(line['Address'])

            category = crud.get_category_by_name(line['Category'])
            print(category)
            # if not category:
            #     crud.create_category(line['Category'])

            #     to store resourec, get category id and store it based on it
            #     resouce takes in 
            
        #     category = line['Category']
        #     org_name = line['Org Name']
        #     contact = line['Contact']
        #     address = line['Address']
        #     location = line['Location']

        # resource = category + org_name+contact+address+location
        # print(resource)