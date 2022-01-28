# -*-coding:utf-8 -*-
import pandas as pd
import numpy as np

output_file = pd.read_csv("./2_multi_query/all_prot_query_screened.csv", header = None, names = ['query acc.', 'strain accs.', 'identity', 'query coverage', 'evalue'])
output_file.to_csv("./2_multi_query/all_prot_query_screened_header.csv", index = False)