# -*-coding:utf-8 -*-
#!/bin/python3

import pandas as pd
import numpy as np
from collections import defaultdict

strain_query = defaultdict(list)
query_list = []
csv_infile = open('all_prot_query_screened_header_40ide_40cov.csv')

next(csv_infile) # 这一步不能少，否则会多出一列

for line in csv_infile:
    query, strain, *other = line.strip().split(',')
    strain = '_'.join(strain.split('_')[0:-1])
    query_list.append(query) if query not in query_list else ''
    strain_query[strain].append(query) if query not in strain_query[strain] else ''

tmp_matrix = np.full((len(strain_query), len(query_list)), 0) # negetive be -1 or 0
out_data = pd.DataFrame(tmp_matrix, columns=query_list, index=list(strain_query.keys()))
for strain in strain_query:
    for query in strain_query[strain]:
        out_data.loc[strain, query] = 1
out_data.to_csv('all_prot_query_screened_header_40ide_40cov_positive_negative.csv')