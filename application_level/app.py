#!/usr/bin/python

import sqlite3 as lite
import os
import sys
from sys import platform
from os import system, path

#insert contents of csv file into the office table
def read_office(con, cur, file_name):
    with open(file_name, 'r') as office:
        non_records = 0
        for row in office:
            cur.execute("INSERT OR IGNORE INTO office values (?,?,?)", row.split(","))
            con.commit()
            non_records += 1
    print('*** {} Records transferred to office! ***'.format(non_records))

#insert contents of csv file into the parties table
def read_parties(con, cur, file_name):
    with open(file_name, 'r') as parties:
        non_records = 0
        for row in parties:
            cur.execute("INSERT OR IGNORE INTO parties values (?,?)", row.split(","))
            con.commit()
            non_records += 1
    print('*** {} Records transferred to parties! ***'.format(non_records))

#insert contents of csv file into the rental agreement table
def read_rental_agreement(con, cur, file_name):
    with open(file_name, 'r') as rental_agreement:
        non_records = 0
        for row in rental_agreement:
            cur.execute("INSERT OR IGNORE INTO rental_agreement values (?,?,?,?)", row.split(","))
            con.commit()
            non_records += 1
    print('*** {} Records transferred to rental_agreement! ***'.format(non_records))

#insert contents of csv file into the customer agency table
def read_customer_agency(con, cur, file_name):
    with open(file_name, 'r') as customer_agency:
        non_records = 0
        for row in customer_agency:
            cur.execute("INSERT OR IGNORE INTO customer_agency values (?,?,?,?,?)", row.split(","))
            con.commit()
            non_records += 1
    print('*** {} Records transferred to customer_agency! ***'.format(non_records))

def main():
    #clear terminal
    if platform == "linux" or platform == "darwin":
        system("clear");
    elif platform == "win32":
        system("cls");

    #intro
    print('SQL COMMAND SHELL');
    print('-----------------------------------------------');
    con = None

    #open db
    try:
        con = lite.connect('../physical_level/GSA.db')
        cur = con.cursor()
    except lite.Error as e:
        print("Error %s:" % e.args[0])
        sys.exit(1)

    #1 for sql command, 2 to add custom csv, 3 clear all tables of data, 4 to quit app
    loop_control = 0
    while(loop_control != '4'):
        print('1. Run SQL commands\n2. Load new csv file\n3. Clean database\n4. Quit')
        loop_control = input('What would you like to do: ')
        while(loop_control != '1' and loop_control != '2' and loop_control != '3' and loop_control != '4'):
            loop_control = input('Try again: ')

        try:
            if(loop_control == '1'):
                run(con, cur)
            if(loop_control == '2'):
                load(con, cur)
            if loop_control == '3':
                clean(con, cur)

        except lite.Error as e:
            print("Error %s:" % e.args[0])
            sys.exit(1)

    # close db
    con.close()

def run(con, cur):
    loop_control = "y"
    while loop_control != "n":
        try:
            #clear terminal
            if platform == "linux" or platform == "darwin":
                system("clear");
            elif platform == "win32":
                system("cls");
    
            #get SQL comand from user input
            myStmt = input('Enter SQL command: ')
            cur.execute(myStmt)
            con.commit()

            #display results
            data = cur.fetchall()
            print("The results are: ")
            for record in data:
                print(record)

        except lite.Error as e:
            print("Error %s:" % e.args[0])

        loop_control = input('Enter another command? (y/n): ')


    #clear terminal
    if platform == "linux" or platform == "darwin":
        system("clear");
    elif platform == "win32":
        system("cls");

def load(con, cur):
    print('1. Office\n2. Parties\n3. Rental agreement\n4. Customer agency')
    table_choice = input('Choose a table to insert data into: ')
    while(table_choice != '1' and table_choice != '2' and table_choice != '3' and table_choice != '4'):
        table_choice = input('Try again: ')

    file_name = input('Please enter the file path to the csv file you would like to use (i.e. ./<file>.csv): ')
    while(os.path.exists(file_name) == False):
        file_name = input('Try again: ')

    if(table_choice == '1'):
        read_office(con, cur, file_name)

    if(table_choice == '2'):
        read_parties(con, cur, file_name)

    if(table_choice == '3'):
        read_rental_agreement(con, cur, file_name)

    if(table_choice == '4'):
        read_customer_agency(con, cur, file_name)

def clean(con, cur):
    #clear all tables
    cur.execute("DELETE FROM office")
    cur.execute("DELETE FROM parties")
    cur.execute("DELETE FROM customer_agency")
    cur.execute("DELETE FROM rental_agreement")
    con.commit()


if __name__ == "__main__":
    main()
