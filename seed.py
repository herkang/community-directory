import os
import json

import crud
import model
import server

os.system('dropdb directs')
os.system('createdb directs')

model.connect_to_db(server.app)
model.db.create_all()

#load data from data/movies.json and save it to a variable:
with open('__location_at_destintion (ex: data/movies.json)') as f:
    resource_data = json.loads(f.read())

resource_in_db = []

for resource in resource_data:
    #TODO: Add datas
    #https://fellowship.hackbrightacademy.com/materials/t2/exercises/ratings-v2/index-2.html
