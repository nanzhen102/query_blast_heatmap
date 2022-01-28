# -*- coding: utf-8 -*-

import pandas as pd
from re import search

input_partial_fname = './2_multi_query/all_prot_query_screened_header_filter_75cov_50aa_positive_negative.csv'
input_full_fname = './2_multi_query/full_name.csv'
output_fname = './2_multi_query/75cov_50aa_output.csv'

input_partial_df = pd.read_csv(input_partial_fname , header=None, index_col = False) # open file with incomplete names
input_full_df = pd.read_csv(input_full_fname , header=None, index_col = False) # open file with complete (full) names

o_df_col_num, o_df_row_num = input_partial_df.shape # rows - columns 
i_df_col_num, i_df_row_num = input_full_df.shape # rows - columns 

for o_row in range(o_df_col_num):   
    o_target = input_partial_df.iloc[o_row,0] # iterate the output_search_col column
    for i_row in range(i_df_col_num):
        i_target = input_full_df.iloc[i_row,0] # the first column of the input file
        if search(o_target,i_target):
            input_partial_df.iloc[o_row,1] = input_full_df.iloc[i_row,1]

input_partial_df.to_csv(output_fname, index_label = False, header = None)
            
    
