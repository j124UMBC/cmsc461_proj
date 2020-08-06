#!/usr/bin/python

import sqlite3 as lite, csv
from sys import platform
from os import system


#READ DATA FROM CSV FILE INTO DATABASE
def read():
    # connect to the databease
    con = lite.connect('../physical_level/GSA.db')
    # create cursor object in order to exectue the SQL code
    cur = con.cursor()
    # open office.csv file
    with open('../application_level/office.csv', 'r') as office:
        non_records = 0
        for row in office:
            cur.execute("INSERT OR IGNORE INTO office values (?,?,?)", row.split(","))
            con.commit()
            non_records += 1
    print('\n{} Record Transferred to office'. format(non_records))
    # open parties.csv file
    with open('../application_level/parties.csv', 'r') as parties:
        non_records = 0
        for row in parties:
            cur.execute("INSERT OR IGNORE INTO parties values (?,?)", row.split(","))
            con.commit()
            non_records += 1
    print('\n{} Record Transferred to parties'. format(non_records))
    # open rental_agreement.csv file
    with open('../application_level/rental_agreement.csv', 'r') as rental_agreement:
        non_records = 0
        for row in rental_agreement:
            cur.execute("INSERT OR IGNORE INTO rental_agreement values (?,?,?,?)", row.split(","))
            con.commit()
            non_records += 1
    print('\n{} Record Transferred to rental_agreement'. format(non_records))
    # open custom_agency.csv file
    # with open('../application_level/customer_agency.csv', 'r') as customer_agency:
    #     non_records = 0
    #     for row in customer_agency:
    #         cur.execute("INSERT OR IGNORE INTO customer_agency values (?,?,?,?,?,?)", row.split(","))
    #         con.commit()
    #         non_records += 1
    # print('\n{} Record Transferred to customer_agency'. format(non_records))
    # con.close()
#READ SQL COMMANDS FROM USER INPUT
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
                for field in record:
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
