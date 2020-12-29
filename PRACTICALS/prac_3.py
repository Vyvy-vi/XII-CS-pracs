# PRACTICAL 3
"""
* Each line in a csv file contains a first name, a second name, a registration number,
* no of years and a department separated by tabs.

? a) Writing a program that copies the contents of the file into a list of tuples.
? b) Displaying:
*        - Full details of the student sorted by registration number.
*        - The names of all students with no of year less than 3.
*        - The number of people in each department.
"""
import csv

# ! Why is this here? (Corona2020- Everyone was using GoogleColab and that needed some special configs to get this to work)
# TODO: Remove this path and switch to normal script.
path = '/content/drive/My Drive/Shared with me/test_set/studentdata.csv'

try:
    f = open(path)
    f.close()
except FileNotFoundError:
    print('Checking local path...')
    path = 'studentdata.csv'
with open(path, mode='r') as f:
    d = csv.reader(f)
    ls = []
    for i in d:
        for k in i:
            s = tuple(k.split(' '))
        ls.append(s)
    print('a) Details copied to a list of tuples:\n')
    print(ls)  # --> a)
    m = {}
    dic = {}
    for i in ls:
        m[i[2]] = ls.index(i)
        if i[-1] not in dic:
            dic[i[-1]] = 1
        else:
            dic[i[-1]] += 1
    k = sorted(m.keys())
    for j in k:
        k[k.index(j)] = ls[m[j]]
    print('b) The details sorted by registration no. are as following:\n')
    print(*k, sep='\n')  # --> b)
    print('b) Names of students with no. of years less than 3:\n')
    for _ in ls:
        if int(_[3]) < 3:
            print(f"{' '.join(_[:2])}")
    print('b) No. of people in each department:\n')
    print(*[i + ':' + str(dic[i]) for i in dic], sep='\n')  # --> b)
