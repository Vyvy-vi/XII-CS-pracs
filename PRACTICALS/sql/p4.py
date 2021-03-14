import os
import mysql.connector
from prettytable import PrettyTable

import tkinter as tk
from tkinter import scrolledtext as st

from dotenv import load_dotenv
load_dotenv()

DB_USER = os.environ['MYSQL_USER']
DB_PASS = os.environ['MYSQL_PASS']

con = mysql.connector.connect(
           host='localhost',
           user=DB_USER,
           password=DB_PASS,
           database='cs_practicals'
          )

cur = con.cursor()

def add_data():
    return
def create_table():
    with open('schema.sql', 'r') as schema:
        res_iter = cur.execute(schema.read(), multi=True)
        con.commit()
def fetch_data():
    cur.execute("SELECT BusNo, Origin, Dest, Rate, Km FROM BUS;")
    table = PrettyTable()
    table.add_rows(cur.fetchall())
    print(table)
    print(type(table))
    return str(table)


def fetch_longest_word():
    word="theword"
    return len(word)+1

def edit(i):
    print(i)

class UserInterface:
    def __init__(self, parent):
        parent.title('BUS GUI')
        tk.Label(parent, text="Bus GUI database management").pack()
        self.scroll_container = tk.Frame(parent)

        self.container1 = tk.Frame(parent)
        self.container1.pack()
        self.data = st.ScrolledText(self.scroll_container, height=40, width= len(fetch_data().split('\n')[0]))
        self.data.pack()
        self.scroll_container.pack()
        self.data.insert(tk.INSERT, fetch_data())
        self.data.configure(state ='disabled')
        self.add_button = tk.Button(self.container1, command=self.add_data)
        self.add_button["text"]= "Add new record"
        self.add_button.grid(row=1, column=0)

        self.refresh_button = tk.Button(self.container1, command=self.refresh_data)
        self.refresh_button["text"] = "Refresh database"
        self.refresh_button.grid(row=1, column=1)
    def add_data(self):
        """function to build interface for adding values and handling addition of new record to db"""
        self.container2 = tk.Frame(self.container1)
        self.container2.grid(row=2, column=0, columnspan=2)

        self.update_label = tk.Label(self.container2, text= "Add new record to the table")
        self.update_label.grid(row=0, column=0, columnspan=2)

        self.bus_no = tk.Label(self.container2)
        self.bus_no['text'] = 'BusNo'
        self.bus_no_entry = tk.Entry(self.container2, width=20)
        self.bus_no.grid(row=1, column=0)
        self.bus_no_entry.grid(row=1, column=1)

        self.origin = tk.Label(self.container2)
        self.origin['text'] = 'Origin'
        self.origin_entry = tk.Entry(self.container2, width=20)
        self.origin.grid(row=2, column=0)
        self.origin_entry.grid(row=2, column=1)

        self.dest = tk.Label(self.container2)
        self.dest['text'] = 'Dest'
        self.dest_entry = tk.Entry(self.container2, width=20)
        self.dest.grid(row=3, column=0)
        self.dest_entry.grid(row=3, column=1)

        self.rate = tk.Label(self.container2)
        self.rate['text'] = 'Rate'
        self.rate_entry = tk.Entry(self.container2, width=20)
        self.rate.grid(row=4, column=0)
        self.rate_entry.grid(row=4, column=1)

        self.km = tk.Label(self.container2)
        self.km['text'] = 'Km'
        self.km_entry = tk.Entry(self.container2, width=20)
        self.km.grid(row=5, column=0)
        self.km_entry.grid(row=5, column=1)

        self.write_data = tk.Button(self.container2, command= self.commit)
        self.write_data["text"] = "Write values to Database"
        self.write_data.grid(row=6, column=0, columnspan=2)
    def refresh_data(self):
        self.data.configure(state='normal')
        self.data.delete(1.0, tk.END)
        self.data.configure(width=len(fetch_data().split('\n')[0]))
        self.data.insert(tk.INSERT, fetch_data())
        self.data.configure(state ='disabled')
if __name__ == '__main__':
    create_table()
    window = tk.Tk()
    gui = UserInterface(window)
    window.mainloop()

