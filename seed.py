import os
import json

import crud
import model
import server

os.system('dropdb directs')
os.system('createdb directs')

model.connect_to_db(server.app)
model.db.create_all()