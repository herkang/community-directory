import os
import csv
import pandas as pd 

import crud
import model
import server

os.system('dropdb directory')
os.system('createdb directory')

model.connect_to_db(server.app)
model.db.drop_all()
model.db.create_all()

with open('db.csv', 'r') as data:

    for line in csv.DictReader(data):

        category = None
        org = None
        contact = None
        address = None
        location = None

        for key, val in line.items():
            # print(line)
            print({key: val})
            print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
       
            if key == "Category":

                category = crud.get_category_by_name(line['Category'])

                if category == None:
                    #TODO create 
                    new_category = create_category

            if key == "Org Name":

            
            if key == "Contact":

            if key == "Address":

            if key == "Location":



            # 
            # if not category:
            #     item = crud.create_category(line['Category'])
                # item = crud.get_category_by_id(line['Category'])
                # print('!!!!!!!!', line['Category'],'!!!!!!!!')
                # !!!!!!!! Latino/as !!!!!!!!             
                # print('!!!!!!!!', item.id,'!!!!!!!!')
                # 5 !!!!!!!!  

            # else:
            #     category_id = crud.get_resources_by_category(item.id)
                
            #     # if not resource:
            #         # category = line['Category']
            #     org_name = line['Org Name']
            #     contact = line['Contact']
            #     address = line['Address']
            #     location = line['Location']
            #     resource_item = crud.create_resource(org_name, contact, address, location, item.id)
