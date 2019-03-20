def ksl(row1):
    l=[]
    if(row1[0]=='0'):
        l.append('111')
        l.append('68')
        return(l)
    else:
        return(row1)
import csv
for i in range(1,76):
    a='subj1log'+str(i)+'.csv'
    with open(a, newline='') as f:
        reader = csv.reader(f)
        row1 = next(reader)
        row1=ksl(row1)
    print(a+','+','.join(row1))
for i in range(1082,1134):
    a='subj17log'+str(i)+'.csv'
    with open(a, newline='') as f:
        reader = csv.reader(f)
        row1 = next(reader)
        row1=ksl(row1)
    print(a+','+','.join(row1))
for i in range(1215,1289):
    a='subj20log'+str(i)+'.csv'
    with open(a, newline='') as f:
        reader = csv.reader(f)
        row1 = next(reader)
        row1=ksl(row1)
    print(a+','+','.join(row1))
for i in range(1453,1501):
    a='subj23log'+str(i)+'.csv'
    with open(a, newline='') as f:
        reader = csv.reader(f)
        row1 = next(reader)
        row1=ksl(row1)
    print(a+','+','.join(row1))
for i in range(1501,1581):
    a='subj24log'+str(i)+'.csv'
    with open(a, newline='') as f:
        reader = csv.reader(f)
        row1 = next(reader)
        row1=ksl(row1)
    print(a+','+','.join(row1))
for i in range(1817,1892):
    a='subj28log'+str(i)+'.csv'
    with open(a, newline='') as f:
        reader = csv.reader(f)
        row1 = next(reader)
        row1=ksl(row1)
    print(a+','+','.join(row1))
for i in range(2046,2123):
    a='subj31log'+str(i)+'.csv'
    with open(a, newline='') as f:
        reader = csv.reader(f)
        row1 = next(reader)
        row1=ksl(row1)
    print(a+','+','.join(row1))
