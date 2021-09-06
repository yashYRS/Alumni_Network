# Program to create necessary tables for the project
import sqlite3

conn = sqlite3.connect('datastored.db')
print("Opened database successfully")

conn.execute('''CREATE TABLE STUDENT
         (REGN_NO INT PRIMARY KEY     NOT NULL,
         BDATE           TEXT    NOT NULL,
         NAME            TEXT     NOT NULL,
         BRANCH            TEXT     NOT NULL,
         EMAIL_ADD 			TEXT NOT NULL,
         CV_LINK        CHAR(50),
         GPA        REAL);''')

conn.execute('''CREATE TABLE ALUMNI
         (USERNAME TEXT PRIMARY KEY     NOT NULL,
         PASSWORD           TEXT    NOT NULL,
         NAME           TEXT    NOT NULL,
         FIELD           TEXT    NOT NULL,
         COMPANY        TEXT,
         POSITION 		TEXT,
         EMAIL_ADD         TEXT);''')

conn.close()
