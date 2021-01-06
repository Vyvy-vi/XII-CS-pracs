# FILE GENERATOR
"""
The purpose of this script is to Generate requisite files for the practicals, inside your sheet.
"""
import csv
print('Generating files...')

# prac-1
with open('file1.txt', 'w+') as fl:
    fl.writelines(['Neither apple nor pine are in pineapple. Boxing rings are square.\n',
                   'Writers write, but fingers don\'t fing. Overlook and oversee are opposites.\n',
                   'A house can burn up as it burns down. An alarm goes off by going on.'])
    fl.seek(0)
    print('File for Practical-1 generated...')

# prac-2
with open('file2-1.txt', 'w+') as fl:
    fl.write('Carry Umbrella and Overcoat When it Rains')
    fl.seek(0)
    print('File for Practical-2 generated...')
# prac-3
with open('studentdata.csv', mode='w', newline='') as f:
    writer = csv.writer(f, delimiter=' ')
    row_list = [["Rajat", "Sen", "12345", "1", "CSEE"],
                ["Jagat", "Narain", "13467", "3", "CSEE"],
                ["Anu", "Sharma", "11756", "2", "Biology"],
                ["Sumita", "Trikha", "23451", "4", "Biology"],
                ["Sumder", "Kumra", "11234", "3", "MME"],
                ["Kanti", "Bhushan", "23211", "3", "CSEE"]]
    writer.writerows(row_list)
    print('File for Practical-5 generated...')

# prac-4
with open('myfile.txt', 'w+') as f:
    f.write(
        'The only person for whom the house was in any way special was Arthur Dent,\n\
and that was only because it happened to be the one he lived in. He had lived in it for about\n\
three years, ever since he had moved out of London because it made him nervous and irritable.\n\
He was about thirty as well, tall, dark-haired and never quite at ease with himself.\n\
The thing that used to worry him most was the fact that people always used to ask him what he was looking so worried about.\n\
He worked in local radio which he always used to tell his friends was a lot more interesting than they probably thought.\n\
It was, too—most of his friends worked in advertising. ')
    print('File for Practical-4 generated...')
# prac-6
with open('placement.csv', mode='w', newline='') as f:
    fields = ["SNO", "NAME", "MARKS1", "MARKS2", "MARKS3", "MARKS4", "MARKS5"]
    writer = csv.DictWriter(f, fieldnames=fields)
    writer.writeheader()
    row_lists = [["1", "JOHN", "4", "3", "4", "2", "5"],
                 ["2", "PETER", "3", "4", "4", "3", "5"]]
    for row_list in row_lists:
        row_dict = {fields[i]: row_list[i] for i in range(len(row_list))}
        writer.writerow(row_dict)
    print('File for Practical-6 generated...')

