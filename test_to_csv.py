import csv
import pandas as pd
import numpy as np
from collections import defaultdict
from re import search

def delete_lines():
    input = open('./all_prot_query.txt', 'r')
    lines = input.readlines()
    output = open("all_prot_query_del_line.txt", "w")
    for line in lines:
        if '#' in line:
            line = line.replace(".", "")
    else:
        output.write(line)

def txt_to_csv():
    input = open("all_prot_query_del_line.txt", "r")
    lines = input.readlines()
    output = open("all_prot_query_del_line.csv", "w")
    spamwriter = csv.writer(output, dialect = 'excel')
    for line in lines:
        line_list = line.strip('\n').split('	')
        spamwriter.writerow(line_list)

if __name__ == "__main__":
    delete_lines()
    txt_to_csv()