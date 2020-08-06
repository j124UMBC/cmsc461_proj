#!/usr/bin/python

import sqlite3 as lite
from sys import platform
from os import system

#READ DATA FROM CSV FILE INTO DATABASE
def read():
    print("reading data from csv file into db")


#START SQL COMMANDS
def start():
    con = None
    try:
        #init db connection
        con = lite.connect('../physical_level/GSA.db')
        cur = con.cursor()

        isEnded = "n"
        while isEnded != "y":
            #clear terminal
            if platform == "linux" or platform == "darwin":
                system("clear");
            elif platform == "win32":
                system("cls");

            #get SQL comand from user input
            myStmt = input('Enter SQL command: ')
            cur.execute(myStmt)

            #display results
            data = cur.fetchall()
            print("The results are: ")
            for record in data:
                for field in rec:
                    print(field,"\t",end='')
            print()
            isEnded = input('Do you want to quit? (y/n): ')

        #commit transaction and close the db connection
        con.commit()
        con.close()

    except lite.Error as e:
        print("Error %s:" % e.args[0])
        sys.exit(1)

if __name__ == "__main__":
    read()
    start()
