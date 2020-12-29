# Practical 15
"""
Create a program to take in a list reg_no, Name,admission_to_class (Nursery, KG, I) and add member functions to
i) Add data to the queue.
ii) Display length of the queue.
iii)Print a report showing number of applications received for admission to each class
"""
q = []


def ui():
    p = int(input('Press 1 to add entry to queue\n\
Press 2 to fetch the record in order\n\
Press 3 to show entire queue of records\n\
Press 4 to show total no. of applications\n\
Press 5 to show no. of applications per class\n\
Press 0 to QUIT.\n'))
    if p == 0:
        print('Bye')
        return
    print()
    if p == 1:
        reg = input('Enter registration no.: \n')
        nm = input('Enter Name: \n')
        cl = input('Enter class being admitted to(Nursery, KG OR I): \n')
        dat = [reg, nm, cl]
        enqueue(dat)
        print('Entry added...\n')
    elif p == 2:
        print(dequeue())
    elif p == 3:
        print(show_q())
    elif p == 4:
        print(f'The no. of applications in record are: {len_q()}')
    elif p == 5:
        print('\n\n', fetch_report(), '\n')
        print()
    ui()


def fetch_report():
    queue_backup = q[::]
    report = {}
    for _ in range(len_q()):
        entry = dequeue()[-1]
        if entry in report:
            report[entry] += 1
        else:
            report[entry] = 1
    report = '\n'.join([f'{i}:{report[i]}' for i in report])
    return report


def show_q():
    val = ''
    for i in q:
        val = val + str(i) + '\n'
    return val


def len_q():
    return len(q)


def enqueue(el):
    q.append(el)


def dequeue():
    return q.pop(0)


ui()
