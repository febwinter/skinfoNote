# basic03.py
import sys
import csv
import os

dir = os.path.dirname(os.path.realpath(__file__))

input_file = dir + '/supplier_data.csv'
output_file = dir + '/output/output3.csv'

filter_date = ['1/20/14', '1/30/14']

with open(input_file, 'r', newline='') as csv_in_file:
    with open(output_file, 'w', newline='') as csv_out_file:
        filereader = csv.reader(csv_in_file) 
        filewriter = csv.writer(csv_out_file)
        header = next(filereader)
        filewriter.writerow(header)
        for row in filereader: 
            # Purchase Date:     1/20/14 or 1/30/14 
            p_date = row[4]
            if p_date in filter_date:
                filewriter.writerow(row)
print('Done.')