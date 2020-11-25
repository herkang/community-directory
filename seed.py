import os
import csv
import pandas as pd 

import crud
import model
import server

os.system('dropdb directory')
os.system('createdb directory')

model.connect_to_db(server.app)
model.db.create_all()

with open('db.csv', 'r') as data:

    for line in csv.DictReader(data):
        for k, v in line.items():
            # print(line)
            # print({k: v})
            category = crud.get_category_by_name(line['Category'])
            if not category:
                item = crud.create_category(line['Category'])
                # item = crud.get_category_by_id(line['Category'])
                # print('!!!!!!!!', line['Category'],'!!!!!!!!')
                # !!!!!!!! Latino/as !!!!!!!!             
                # print('!!!!!!!!', item.id,'!!!!!!!!')
                # 5 !!!!!!!!  
            else:
                category_id = crud.get_resources_by_category(item.id)

                # if not resource:
                    # category = line['Category']
                org_name = line['Org Name']
                contact = line['Contact']
                address = line['Address']
                location = line['Location']
                resource_item = crud.create_resource(org_name, contact, address, location, item.id)

