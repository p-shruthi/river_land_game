def get_files():
    import csv
    global name_list
    global email_list
    name_list = []
    email_list = []
    with open('Task_Training_Data.csv') as csvfile:
        readCSV = csv.reader(csvfile)
        for row in readCSV:
            name_list.append(row[0])
            email_list.append((row[1]))
        print('The data is read from CSV File')
get_files()