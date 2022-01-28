import csv
import pandas as pd
import numpy as np
from collections import defaultdict
from re import search

def delete_lines(input_fname,output_fname):
    input = open(input_fname, 'r')
    output = open(output_fname, "w")

    lines = input.readlines()
    for line in lines:
        if '#' in line:
            line = line.replace(".", "")
        else:
            output.write(line)
    input.close()
    output.close()

def txt_to_csv(input_fname, output_fname):
    input = open(input_fname, "r")
    lines = input.readlines()
    output = open(output_fname, "w")
    spamwriter = csv.writer(output, dialect = 'excel')
    for line in lines:
        line_list = line.strip('\n').split('	')
        spamwriter.writerow(line_list)

def header_add(input_fname,output_fname):
    output_file = pd.read_csv(input_fname, header = None, names = ['query acc.', 'strain accs.', 'identity', 'query coverage', 'evalue'])
    output_file.to_csv(output_fname, index = False)

def data_filter(input_fname, output_fname):
    input_file = pd.DataFrame(pd.read_csv(input_fname, header = 0))

    mask=((input_file["identity"]>=50) & (input_file["query coverage"]>= 75))
    input_file=input_file.loc[mask] 

    input_file.to_csv(output_fname, index = False) 

def pos_neg(input_fname, output_fname):
    strain_query = defaultdict(list)
    query_list = []
    csv_infile = open(input_fname)

    next(csv_infile) # 这一步不能少，否则会多出一列

    for line in csv_infile:
        query, strain, *other = line.strip().split(',')
        strain = '_'.join(strain.split('_')[0:-1])
        query_list.append(query) if query not in query_list else ''
        strain_query[strain].append(query) if query not in strain_query[strain] else ''

    tmp_matrix = np.full((len(strain_query), len(query_list)), 0)
    out_data = pd.DataFrame(tmp_matrix, columns=query_list, index=list(strain_query.keys()))
    for strain in strain_query:
        for query in strain_query[strain]:
            out_data.loc[strain, query] = 1
    out_data.to_csv(output_fname)
