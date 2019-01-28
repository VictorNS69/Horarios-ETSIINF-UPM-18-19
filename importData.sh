#!/bin/bash

# Simple script to load all the information in the /ImportData/data.dat
# into the database "db.sqlite3"

cd ImportData
python import_data.py
cd ..
echo "Creating superuser for the database"
echo "If you dont want to create a super user, press Ctrl-C"
./manage.py createsuperuser

