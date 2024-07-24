import csv
with open("data/newfile.csv") as f:
    reader = csv.reader(f)
    header_row = next(reader) #the next() method to obtain the header. The .next() method returns the current row and moves to the next row.
    print(header_row)
    for index,coloumn_header in enumerate(header_row):
        print(index, coloumn_header)
    names = []
    for row in reader:
        name = row[1]
        names.append(name)
    print(names)