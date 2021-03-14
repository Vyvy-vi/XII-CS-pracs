import os
import mysql.connector
from prettytable import PrettyTable

import tkinter as tk
from tkinter import scrolledtext as st
from tkinter import messagebox

from dotenv import load_dotenv
load_dotenv()

DB_USER = os.environ['MYSQL_USER']
DB_PASS = os.environ['MYSQL_PASS']

class DataLayer:
    def __init__(self):
        self.con = mysql.connector.connect(
                         host='localhost',
                         user = DB_USER,
                         password = DB_PASS,
                         database='cs_practicals'
                   )
        self.cur = self.con.cursor()
    def fetch_data(self):
        self.cur.close()
        self.cur = self.con.cursor()
        self.cur.execute("SELECT BusNo, Origin, Dest, Rate, Km FROM BUS;")
        table = PrettyTable()
        table.field_names = ["BusNo", "Origin", "Dest", "Rate", "Km"]
        table.add_rows(self.cur.fetchall())
        print(table)
        return str(table)
    def create_table(self):
        with open('schema.sql', 'r') as schema:
            queries = self.cur.execute(schema.read(), multi=True)
            for query in queries:
                print(query)
                print(f'{query.rowcount} rows affected')
            self.con.commit()
    def update_data(self, data):
        self.cur.close()
        self.cur = self.con.cursor()
        try:
            self.cur.execute("INSERT INTO BUS VALUES(%s, %s, %s, %s, %s)",
                    (data[0],
                     data[1],
                     data[2],
                     data[3],
                     data[4],
                    ))
            self.con.commit()
            messagebox.showinfo('SUCCESS', 'Successfully added to db')

        except Exception as e:
            if isinstance(e, mysql.connector.errors.IntegrityError):
                messagebox.showerror('ERROR', f'Record with BusNo={data[0]} exists...\nPlease Try again.')
        print(self.fetch_data)
class UserInterface:
    def __init__(self, parent):
        parent.title('BUS GUI')
        tk.Label(parent, text="Bus GUI database management").pack()
        self.scroll_container = tk.Frame(parent)

        self.container1 = tk.Frame(parent)
        self.container1.pack()
        self.data = st.ScrolledText(self.scroll_container, height=40, width= len(DataLayer().fetch_data().split('\n')[0]))
        self.data.pack()
        self.scroll_container.pack()
        self.data.insert(tk.INSERT, DataLayer().fetch_data())
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

        self.write_data = tk.Button(self.container2, command= self.commit_data)
        self.write_data["text"] = "Write values to Database"
        self.write_data.grid(row=6, column=0, columnspan=2)
    def refresh_data(self):
        self.data.configure(state='normal')
        self.data.delete(1.0, tk.END)
        self.data.configure(width=len(DataLayer().fetch_data().split('\n')[0]))
        self.data.insert(tk.INSERT, DataLayer().fetch_data())
        self.data.configure(state ='disabled')
    def commit_data(self):
        bus_no = self.bus_no_entry.get()
        origin = self.origin_entry.get()
        dest = self.dest_entry.get()
        rate = self.rate_entry.get()
        km = self.km_entry.get()
        data = [bus_no, origin, dest, rate, km]
        DataLayer().update_data(data)

if __name__ == '__main__':
    DataLayer().create_table()
    window = tk.Tk()
    gui = UserInterface(window)
    window.mainloop()

