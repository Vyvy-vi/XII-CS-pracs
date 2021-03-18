import datetime
import mysql.connector

db_user = os.environ.get('DB_USER')
db_pass = os.environ.get('DB_PASS')
mydb = mysql.connector.connect(
                      host = 'localhost',
                      user = db_user,
                      password = db_pass,
                      database = 'mydb' )
cur = mydb.cursor()
def menu():
    print('The following database actions can be performed:\n\
1- Add a new record to the table\n\ 2- Update a student\'s record in the table\n\
3- EXIT')
    option = int(input('Select option[1/2/3]: '))
    if option == 1:
        add_record() #-> i)
    elif option == 2:
        update_record()
    elif option == 3:
        mydb.close()
        print('Bye')
        return
    else:
        print('There seems to be an error in the option you selected\nPlease Try again…')
    menu()
def add_record():
    roll = int(input('Enter Roll No. = '))
    name = str(input('Enter Name(max 30 chars) = '))
    _class = str(input('Enter class(numerical, press <Enter> to leave this field empty) = '))
    dob = str(input('Enter Date(YYYY-MM-DD, press <Enter> to leave empty) = '))
    gender = str(input('Enter Gender(press <Enter> to leave empty)= '))
    cols = ['RollNo', 'Name']
    vals = [roll, name]
    if gender != '':
        cols.append('Gender')
        vals.append(gender)
    if _class != '':
        cols.append('Class')
        vals.append(int(_class))
    if dob != '':
        dob = dob.split('-')
        dob = datetime.date(dob[0], dob[1], dob[2]).isoformat()
        cols.append('DOB')
        vals.append(dob)
    cols = str(tuple(cols)).replace("\'", "")
    vals = str(tuple(vals))
    QUERY = "INSERT INTO STUDENT %s VALUES %s;" % (cols, vals)
    cur.execute(QUERY)
    print('Values added')
def update_record():
    roll = int(input('Enter the RollNo. for the student\'s record that you want to edit: '))
    cur.execute("SELECT * FROM STUDENT WHERE RollNo = '%s'" % (roll))
    print('Existing data\n', cur.fetchall())
    name = str(input('Enter new Name(max 30 chars, press <Enter> to leave unchanged) = '))
    _class = str(input('Enter Class(numerical, press <Enter> to leave this field unchanged) = '))
    dob = str(input('Enter Date(YYYY-MM-DD, press <Enter> to leave unchanged) = '))
    gender = str(input('Enter Gender(press <Enter> to leave unchanged)= '))
    cols = []
    vals = []
    if name != '':
        cols.append['Name'] = str(name)
    if gender != '':
        cols['Gender'] = gender
    if _class != '':
        cols['Class'] = int(class)
    if dob != '':
        dob = dob.split('-')
        dob = datetime.date(dob[0], dob[1], dob[2]).isoformat()
        cols['DOB'] = dob
        for i in cols:
            cur.execute(f"UPDATE STUDENT SET {i} = %s WHERE RollNo = %s", (cols[i], roll))
            mydb.commit()
        cur.execute("SELECT * FROM STUDENT WHERE RollNo = '%s'" % (roll))
        print('The records have been updated\nNew data:n', cur.fetchall()) 
 

