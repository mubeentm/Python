import csv



with open('portfolio1.csv',mode='w') as pfile:
    pfile_writer = csv.writer(pfile,delimiter=",",quotechar='"',quoting=csv.QUOTE_MINIMAL)
    pfile_writer.writerow(['Infosys',10,2700])
    pfile_writer.writerow(['UST', 5, 3200])

with open('portfolio.csv') as pfile:
    csv_reader = csv.reader(pfile,delimiter=",")
    line_count=0
    for row in csv_reader:
        if line_count==0:
            print(f'column names are {",".join(row)}')
            line_count+=1
        else:
            print(f'\t{row[0]} has {row[1]} no. of shares at price {row[2]}')
            line_count+=1
    print(f'Read {line_count-1} shares from the portfolio')