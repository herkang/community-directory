from bs4 import BeautifulSoup
import requests

source = requests.get('https://www.stcloudstate.edu/mrc/outreach/mn-orgs.aspx').text


soup = BeautifulSoup(source, 'lxml')
#whole webpage
#print(soup.prettify())

table = soup.find('tbody')
#all table content in html pretiffy and links
#print(table.prettify())

summary = table.find_all('tr')
#similiar to table above, but can't prettify
#print(summary)

def data(summary):
    for row in summary:

        return row_data = [td.text for td in row.find_all('td')]


resource_obj = table.tr.text
#one resource object
#print(resource_obj)

category = soup.find('tbody').td.text
#print one race category
#print(category)
