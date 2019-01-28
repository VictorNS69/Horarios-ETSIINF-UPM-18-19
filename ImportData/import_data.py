import sqlite3
import DataObject
import os
import subprocess
import shlex


def main():
    """
    Main program that creates the db and imports the data from the data.dat file
    :return: Creates a db.sqlite3 database
    """
    if os.path.isfile('../db.sqlite3'):
        print("This will delete the db.sqlite3 database you have now")
        yes = {'yes', 'y', 'ye', ''}
        no = {'no', 'n'}
        inp = input("Are you agree? [Y/n]: ").lower()
        if inp in yes:
            print("Deleting db.sqlite3")
            os.remove("../db.sqlite3")
            print("db.sqlite3 removed")
        elif inp in no:
            print("Import cancelled\nExiting")
            exit(0)
        else:
            print("This is not a valid value.\nExiting.")
            exit(0)

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
        to_string = to_string.replace("\"", "")
        cur.execute("INSERT INTO ScheduleGenerator_subject (type, semester, schedules, ects, code, name ) "
                    "VALUES(\'" + str(item.type).upper() + "\', " + str(item.semester) + ", \'" + to_string.upper() + "\',\' " +
                    str(item.ects) + "\',\' " + str(item.code) + "\', \'" + str(item.name).upper() + "\');")
        con.commit()
    print("Database created as db.sqlite3")

    con.close()
    print("Closed connection with the database")
    exit(0)


if __name__ == "__main__":
    main()
