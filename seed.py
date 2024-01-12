import os
import crud
import server
import model
from datetime import date, time, timezone

os.system("dropdb sports")
os.system("createdb sports")

model.connect_to_db(server.app)
model.db.create_all()