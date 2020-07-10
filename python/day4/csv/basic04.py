# basic04.py
import sys, csv
import re
import os

dir = os.path.dirname(os.path.realpath(__file__))

input_file = dir + '/supplier_data.csv'
output_file = dir + '/output/output4.csv'

# 001- 
pattern = re.compile(r'(?P<my_pattern_group>^001-.*)', re.I) # 정규표현식으로 패턴 적용해 데이터 찾아냄

with open(input_file, 'r', newline='') as csv_in_file:
    with open(output_file, 'w', newline='') as csv_out_file:
        filereader = csv.reader(csv_in_file) 
        filewriter = csv.writer(csv_out_file)
        header = next(filereader)
        filewriter.writerow(header)
        for row in filereader: 
            invoice_number = row[1]
            # match, search, find -> 맞는 패턴만 출력
            if pattern.search(invoice_number):
                filewriter.writerow(row)

print('Done.')