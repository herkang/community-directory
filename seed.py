import os
import csv

import crud
import model
import server

os.system('dropdb directory')
os.system('createdb directory')

model.connect_to_db(server.app)
model.db.drop_all()
model.db.create_all()

with open('static/database.cvs', 'r') as data:

    for line in csv.DictReader(data):

        cat_name = None
        org = None
        contact = None
        address = None
        location = None

        for key, val in line.items():

            if key == "Category":

                cat_name = line['Category']

                if crud.get_category_by_id(cat_name) == []:
                
                    crud.create_category(val)
    
            elif key == "Org Name":
                org = val
            
            elif key == "Contact":
                contact = val
                
            elif key == "Address":
                address = val

            else: 
                location = val

        crud.create_resource(org_name=org, contact=contact, address=address, location=location, category_id=cat_name)
         