# -*-coding:utf-8 -*-
#!/bin/python3

import pandas as pd
import numpy as np
from collections import defaultdict

strain_query = defaultdict(list)
query_list = []
strain_list = []
strain_seq_list = []
csv_infile = open('all_prot_query_screened_header_40ide_40cov.csv')

next(csv_infile) # 这一步不能少，否则会多出一列


for line in csv_infile:
    query, strain_seq, *other = line.strip().split(',') # the column for query and strain_seq
    strain = '_'.join(strain_seq.split('_')[0:-1]) # the strain name
    query_list.append(query) if query not in query_list else '' # get all query name without duplicates
    strain_list.append(strain) if strain not in strain_list else ''
    strain_seq_list.append(strain_seq) if strain_seq not in strain_seq_list else ''
    
    strain_query[strain_seq].append(query) if query not in strain_query[strain] else ''
    # print(strain_query[strain])

# tmp_matrix = np.full((len(strain_query), len(query_list)), 0) # negetive be -1 or 0
# out_data = pd.DataFrame(tmp_matrix, columns=query_list, index=list(strain_query.keys()))
# for strain in strain_query:
#     for query in strain_query[strain]:
#         out_data.loc[strain, query] = 1
# out_data.to_csv('all_prot_query_screened_header_40ide_40cov_positive_negative.csv')