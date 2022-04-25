import csv

with open('./data/product.csv', 'r') as inp:
    reader = csv.DictReader(inp, delimiter=';')
    for line_dict in reader:
        op = int(line_dict['Old price'])
        np = int(line_dict['New price'])
        if op > np:
            print(line_dict['Name'])