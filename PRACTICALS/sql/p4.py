import os
import mysql.connector

import tkinter as tk
from dotenv import load_dotenv

load_dotenv()

#  DB_USER = os.envoron['MYSQL_USER']
#  DB_PASS = os.environ['MYSQL_PASS']
#
#  con = mysql.connector.connect(
#          host='localhost',
#          user=DB_USER,
#          password=DB_PASS,
#          database='cs_practicals'
#         )
#
# cur = con.cursor()

def delete():
    return
def edit():
    return
def query():
    return
def create_table():
    return
def fetch_data():
    return

def edit(i):
    print(i)
class UserInterface:
    def __init__(self, parent):
        parent.title('BUS GUI')
        self.container1 = tk.Frame(parent)
        self.container1.pack()

        self.add_button = tk.Button(self.container1)
        self.add_button["text"]= "Add new record"
        self.add_button["command"] = edit(id)
        self.add_button.grid(row=0, column=0)

        self.refresh_button = tk.Button(self.container1)
        self.refresh_button["text"] = "Refresh database"
        self.refresh_button.grid(row=0, column=1)
if __name__ == '__main__':
    window = tk.Tk()
    gui = UserInterface(window)
    window.mainloop()

