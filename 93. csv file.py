from csv import reader
f=open('file.csv',mode='r')
csv_reader=reader(f)
for row in csv_reader:
    print(row)
