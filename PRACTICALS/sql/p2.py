import os
import mysql.connector
db_user = os.environ.get('DB_USER')
db_pass = os.environ.get('DB_PASS')

mydb = mysql.connector.connect(host='localhost',
                               user=db_user,
                               password=db_pass,
                               database='mydb')
cur = mydb.cursor()
# i)
cur.execute("CREATE TABLE ITEM(Itemcode VARCHAR(255), Itemname VARCHAR(255), Price FLOAT)") 
# ii) ---menu-driven-system---


def menu():
    print('The following database actions can be performed:\n\
1 - Add a new item to the table\n\
2 - See a list of all items from the table\n\
3 - Search for records on the basis of Itemcode\n\
4 - EXIT')


option = int(input('Select option[1/2/3/4]: '))
if option == 1:
    print('Enter respective values for the colums. To leave the column empty, press < Enter >')
    code = str(input('code= '))
    name = str(input('name='))
    price = str(input('price= '))
    # clean data
    code = str(code) if code != '' else None
    name = str(name) if name != '' else None
    price = float(price) if price != '' else None
    insert_record(Itemcode=code, Itemname=name, Price=price)
elif option == 2:
    print('list of all records')
    print(fetch_records())
elif option == 3:
    code = str(input(
        'Enter value of Itemcode for the item you want the details of: Itemcode= '))
    print(fetch_records(Itemcode=code))
elif option == 4:
    mydb.close()
    print('Bye')
    return
else:
    print('Their seems to be something wrong here. Please Try Again….')

menu()


def insert_record(table='ITEM', Itemcode=None, Itemname=None, Price=None):
    cols = []
    vals = []
    if Itemcode:
        cols.append('Itemcode')
        vals.append(str(Itemcode))
    if Itemname:
        cols.append('Itemname')
        vals.append(str(Itemname))
    if Price:
        cols.append('Price')
        vals.append(float(Price))
    cols = str(tuple(cols)).replace("\'", "")
    vals = str(tuple(vals))
    QUERY = "INSERT INTO % s % s VALUES % s; " % (table, cols, vals)
    cur.execute(QUERY)
    mydb.commit()
    print(cur.rowcount, "record inserted")


def fetch_records(table= “ITEM”, Itemcode=None):
    if Itemcode:
        QUERY = "SELECT * FROM % s WHERE Itemcode='% s'" % (table, Itemcode)
    else:
        QUERY = "SELECT * FROM % s" % (table)
        cur.execute(QUERY)
        print('Fetched Records')
        return cur.fetchall()
