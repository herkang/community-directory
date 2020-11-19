from bs4 import BeautifulSoup
import requests
from bs2json import bs2json

source = requests.get('https://www.stcloudstate.edu/mrc/outreach/mn-orgs.aspx').text


soup = BeautifulSoup(source, 'lxml')
#whole webpage
#print(soup.prettify())

# converter = bs2json()

# tag = soup.find('td')
# json = converter.convert(tag)
# print(json)



table = soup.find('tbody')
#all table content in html pretiffy and links
#print(table.prettify())

summary = table.find_all('tr')
#similiar to table above, but can't prettify
#print(summary)

# def data(summary):

#     item_in_list = []
#     for row in summary:
#         for td in row.find_all('td'):
#             item_in_list.append(td.text)
#     return item_in_list

