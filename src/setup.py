'''
1. Connect to the database
2. Create the tables
3. Insert primary password
'''

import sqlite3 
from os import environ, mkdir, path
from sys import platform
from .Encryption import hash

fileName = "Passwords.db"
pathName = None
if platform.lower().startswith("win"):
    pathName = f"{environ['APPDATA']}\\SimplePasswordManager"
else:
    pathName = f"{environ['HOME']}/.config/SimplePasswordManager" 
if not path.exists(pathName):    
    mkdir(pathName)
fileName = path.join(pathName, fileName)

def setupDatabase(primaryPassword):
    conn = sqlite3.connect(fileName)
    cur = conn.cursor()

    # Create the table 
    createTableSyntax = [
        '''
        CREATE TABLE "Passwords" (
	        "email"	TEXT,
	        "website"	TEXT,
        	"password"	TEXT,
        	PRIMARY KEY("email","website")
        );
        ''',
        '''
        CREATE TABLE "PrimaryPassword" (
	        "password"	TEXT
        );
        '''
    ]

    for syntax in createTableSyntax:
        cur.execute(syntax)
        conn.commit()

    # Insert the primary password

    syntax = f"INSERT INTO PrimaryPassword('password') VALUES('{hash(primaryPassword)}');"
    cur.execute(syntax)
    conn.commit()

    cur.close()
    conn.close()
