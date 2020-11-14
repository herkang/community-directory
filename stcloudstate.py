from bs4 import BeautifulSoup
import requests
from bs2json import bs2json

source = requests.get('https://www.stcloudstate.edu/mrc/outreach/mn-orgs.aspx').text


soup = BeautifulSoup(source, 'lxml')
#whole webpage
#print(soup.prettify())

converter = bs2json()

tag = soup.find('td').text
json = converter.convert(tag)
print(json)



# table = soup.find('tbody')
# #all table content in html pretiffy and links
# #print(table.prettify())

# summary = table.find_all('tr')
# #similiar to table above, but can't prettify
# #print(summary)

# def data(summary):
#     for row in summary:
#         row_data = [td.text for td in row.find_all('td')]

#         print(row_data)

# resource_obj = table.tr.text
# #one resource object
# #print(resource_obj)

# category = soup.find('tbody').td.text
# #print one race category
# #print(category)
