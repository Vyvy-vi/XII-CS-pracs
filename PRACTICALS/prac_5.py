# PRACTICAL 5
"""
A dictionary Customer contains the following keys {roomno,name,duration}
A binary file “hotel.dat” contains details of customer checked in the hotel.
Write Code in python to perform the following using pickle module
(i) Read n dictionary objects and load them into the file
(ii) Read all the dictionary objects from the file and print them
(iii) Counts the number of customers present in the hotel.
(iv) Display those customers from the file, who have stayed more than 2 days in the hotel.
"""
import pickle
ROOM = []


def ui():
    print('\nWelcome to pickle module example customer query system (using binary files)')
    print('1- add dictionary objects \n\
2- Read and print all customer data(all dictionary objects) \n\
3- Count no. of customers in the hotel \n\
4- Display customers that have stayed longer than 2 days. \n\
5- Quit program')
    index = input('Enter index no. corresponding to your desired action: ')
    if index == '5':
        print('Terminating...')
        return
    elif index == '1':
        add()
    elif index == '2':
        print('\n All costumer data in the records: \n')
        logd(2)
    elif index == '3':
        cnt()
    elif index == '4':
        stay2()
    else:
        print('invalid code')
    ui()


def add():  # --> (i)
    with open('hotel.dat', 'wb') as f:
        n = int(input("No. of records to be added: "))
        for _ in range(n):
            tup = input(
                "Enter records one by one with fields seperated by spaces (room-no. name duration): ").split(' ')
            # --> Unique room no. check not necessary, but added for error handling
            global ROOM
            if tup[0] not in ROOM:
                ROOM.append(tup[0])
            else:
                print('ERROR... That room no. seems to be occupies')
                return
            tup[-1] = int(tup[-1])
            customer = dict(zip(('Room No.', 'Name', 'Duration'), tuple(tup)))
            pickle.dump(customer, f)
        print('records added...')


def logd(x):  # --> (ii)
    if x == 0:
        num = 0
    elif x == 1:
        L = []
    with open('hotel.dat', 'rb') as f:
        while True:
            try:
                d = pickle.load(f)
                num = num + \
                    1 if x == 0 else L.append(d) if x == 1 else print(d)
            except BaseException:
                break
        if x == 0:
            return num
        elif x == 1:
            return L


def cnt():
    print('\nNo. of customers in the hotel')
    print(logd(0))


def stay2():
    print("\nCustomers who have stayed longer than 2 days:")
    L = logd(1)
    L = [i for i in L if i['Duration'] > 2]
    print(_ for _ in L)


ui()
