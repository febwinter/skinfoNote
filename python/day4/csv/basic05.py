# basic05.py
import sys, csv
import re
import os

dir = os.path.dirname(os.path.realpath(__file__))

input_file = dir + '/supplier_data.csv'
output_file = dir + '/output/output5.csv'

my_columns = [0, 3] # 0번 col과 3번 col만 추출하려 한다.

with open(input_file, 'r', newline='') as csv_in_file:
    with open(output_file, 'w', newline='') as csv_out_file:
        filereader = csv.reader(csv_in_file) 
        filewriter = csv.writer(csv_out_file)
        for row in filereader: 
            row_list_output = []
            for index_value in my_columns:
                row_list_output.append(row[index_value])
            filewriter.writerow(row_list_output)
print('Done.')