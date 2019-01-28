import sqlite3
import DataObject as DO

def main():
    
    print("Extracting data")
    data_o = DO.DataObject()
    data_o.make_attributes()
    print("Data extracted")
    print("Connecting to the database")
    con = sqlite3.connect("../db.sqlite3")
    cur = con.cursor()
    print("Established connection")
    cur.execute("SELECT *  FROM ScheduleGenerator_subject WHERE name = 'FUNDAMENTOS FISICOS Y TECNOLOGICOS DE LA INFORMATICA';")
    print(cur.fetchone())


if __name__ == "__main__":
    main()
