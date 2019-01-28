#!/bin/bash

# Simple script to load all the information in the /ImportData/data.dat
# into the database "db.sqlite3"

cd ImportData
python import_data.py
cd ..

