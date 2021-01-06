import csv

f=open('placement.csv','r')
reader=csv.reader(f)
for line in reader:
    print(line)

def total_people():
    i=0
    f.seek(0)
    for rec in reader:
        if rec[0]=='SNO':
            pass
        else:
            i=i+1
    return i

def top():
    n=int(input("Enter no. for top 'n' names: "))
    d={}
    l=[]
    f.seek(0)
    for lst in reader:
        if lst[0]=='SNO':
            pass
        else:
            total=0
            for m in range (2,7):
                total=total+int(lst[m])
            l.append(total)
            d[lst[1]]=total
    l.sort(reverse=True)
    l2=l[0:n]
    print("\n")
    print("Top",n,"people:")
    for element in l2:
        for key in d:
            if d[key]==element:
                print(key,'(marks:',d[key],')')
print("\n")
print("Total no. of people:",total_people())
top()
