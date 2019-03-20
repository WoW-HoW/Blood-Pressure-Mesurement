def ksl(row1):
    l=[]
    if(row1[0]=='0'):
        l.append('100')
        l.append('50')
        return(l)
    else:
        return(row1)
import csv
for i in range(456,516):
    a='subj8log'+str(i)+'.csv'
    with open(a, newline='') as f:
        reader = csv.reader(f)
        row1 = next(reader)
        row1=ksl(row1)
    print(a+','+','.join(row1))
for i in range(728,795):
    a='subj12log'+str(i)+'.csv'
    with open(a, newline='') as f:
        reader = csv.reader(f)
        row1 = next(reader)
        row1=ksl(row1)
    print(a+','+','.join(row1))
for i in range(795,847):
    a='subj13log'+str(i)+'.csv'
    with open(a, newline='') as f:
        reader = csv.reader(f)
        row1 = next(reader)
        row1=ksl(row1)
    print(a+','+','.join(row1))
for i in range(927,1002):
    a='subj15log'+str(i)+'.csv'
    with open(a, newline='') as f:
        reader = csv.reader(f)
        row1 = next(reader)
        row1=ksl(row1)
    print(a+','+','.join(row1))
for i in range(1186,1215):
    a='subj19log'+str(i)+'.csv'
    with open(a, newline='') as f:
        reader = csv.reader(f)
        row1 = next(reader)
        row1=ksl(row1)
    print(a+','+','.join(row1))
for i in range(1892,1971):
    a='subj29log'+str(i)+'.csv'
    with open(a, newline='') as f:
        reader = csv.reader(f)
        row1 = next(reader)
        row1=ksl(row1)
    print(a+','+','.join(row1))
