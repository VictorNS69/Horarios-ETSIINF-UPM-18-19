import sqlite3
import DataObject
import os
import subprocess
import shlex


def main():
    if os.path.isfile('../db.sqlite3'):
        print("This will erase the db.sqlite3 database you have now")
        inp = input("Are you agree? [Y/n]: ")
        if inp == "YES" or "yes" or "y" or "Y":
            print("Deleting db.sqlite3")
            os.remove("../db.sqlite3")
            print("db.sqlite3 removed")
        elif inp == "NO" or "no" or "n" or "N":
            print("Import cancelled\nExiting")
            exit(1)
        else:
            print("This is not a valid value.\nExiting.")
            exit(1)

    print("Extracting data")
    subjects = DataObject.make_attributes()
    print("Data extracted")

    print("Connecting to the database")
    con = sqlite3.connect("../db.sqlite3")
    cur = con.cursor()
    print("Established connection")

    print("Creating the database")
    subprocess.call(shlex.split('../manage.py makemigrations'))
    subprocess.call(shlex.split('../manage.py migrate'))
    print("Importing data")
    for item in subjects:
        to_string = str(item.schedules)
        to_string = to_string.replace("{", "\"")
        to_string = to_string.replace("}", "\"")
        to_string = to_string.replace("'", "")
        cur.execute("INSERT INTO ScheduleGenerator_subject (type, semester, schedules, ects, code, name ) "
                    "VALUES(\'" + str(item.type) + "\', " + "1" + ", \'" + to_string + "\',\' " + str(item.ects) + "\',\' "
                    + str(item.code) + "\', \'" + str(item.name) + "\');")
        con.commit()
    print("Database created as db.sqlite3")


if __name__ == "__main__":
    main()
