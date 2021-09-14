'''
1. Do the login
2. If the login is successful, use the working class
3. Else, no access allowed.
'''

import sqlite3
from .setup import fileName 
from .Encryption import *

class Working:
    def __init__(self, primaryPassword: str):
        self.conn = sqlite3.connect(fileName)
        self.cur = self.conn.cursor()

        self.cur.execute("SELECT password FROM PrimaryPassword;")
        hashFromDatabase = self.cur.fetchall()[0][0]

        if hashFromDatabase == hash(primaryPassword):
            # Login successful.
            self._privateKey = hashEnc(primaryPassword)
            self.loginStatus = True # True means successful login.
        else:
            self.loginStatus = False
            self._privateKey = None 

    def changePrimaryPassword(self, oldPassword: str, newPassword: str) -> bool:
        self.cur.execute("SELECT password FROM PrimaryPassword;")
        hashFromDatabase = self.cur.fetchall()[0][0]

        if hashFromDatabase == hash(oldPassword):
            # Can change password.
            self.cur.execute(f"UPDATE PrimaryPassword SET password = '{hash(newPassword)}' WHERE password = '{hash(oldPassword)}';")
            self.conn.commit()
            entries = self.seeEntries()
            newKey = hashEnc(newPassword)

            for entry in entries:
                self.cur.execute(f"UPDATE Passwords SET password = '{encrypt(self.getEntry(entry[0], entry[1]), newKey)}' WHERE (email = '{entry[0]}' AND website = '{entry[1]}');")
                self.conn.commit()
            
            self._privateKey = newKey
            return True
        else:
            return False 

    def getEntry(self, email: str, website: str) -> str:
        if self.loginStatus:    
            try:    
                self.cur.execute(f"SELECT password FROM Passwords WHERE (email = '{email}' AND website = '{website}');")
                encryptedData = self.cur.fetchall()[0]
                return decrypt(encryptedData[0], self._privateKey)
            except Exception:
                return ""
        return ""

    def putEntry(self, email: str, website: str, password: str) -> bool:
        if self.loginStatus:
            try:
                self.cur.execute(f"INSERT INTO Passwords (email, website, password) VALUES ('{email}', '{website}', '{encrypt(password, self._privateKey)}');")
                self.conn.commit()
                return True
            except Exception as e:
                return False
        return False

    def updateEntry(self, oldEmail: str, oldWebsite: str, email: str, website: str, password: str) -> None:
        if self.loginStatus:    
            self.cur.execute(f"UPDATE Passwords SET email = '{email}', website = '{website}', password = '{encrypt(password, self._privateKey)}' WHERE (email = '{oldEmail}' AND website = '{oldWebsite}');")
            self.conn.commit()

    def seeEntries(self):
        if self.loginStatus:    
            self.cur.execute("SELECT email, website FROM Passwords;")
            return self.cur.fetchall()
            # To return in format of (email, website) tuple.
        else:
            return []

    def __del__(self):
        self.loginStatus = False
        self.cur.close()
        self.conn.close()