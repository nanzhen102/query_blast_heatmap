# -*- coding: utf-8 -*-

import pandas as pd
from re import search

input_partial_fname = '01_node_label.csv'
input_full_fname = './full_name_type_strain_DB_Sep26_2022.csv'
# input_gene_df = pd.read_csv("../query_info.csv", header = 0, index_col = 0) # open query_gene.csv

output_fname = input_partial_fname.split(".")[0]  + "_species_matched.csv"

input_partial_df = pd.read_csv(input_partial_fname , header=None, index_col = False) # open file with incomplete names
input_full_df = pd.read_csv(input_full_fname , header=None, index_col = False) # open file with complete (full) names


part_df_row_num, part_df_col_num = input_partial_df.shape # rows - columns 
ful_df_row_num, ful_df_col_num = input_full_df.shape # rows - columns 
# gene_df_row_num, gene_df_col_num = input_gene_df.shape

input_partial_df.insert(loc=1, column="species", value="not_nan") # insert a column - to write the matched species name
input_partial_df.insert(loc=2, column="sum_up", value=1) # insert a column - to calculate the proportion

if pd.isna(input_partial_df.iloc[0,0]) == True: # in pos_neg csv, the first column of the first row is nan, thus need to fill a value
    input_partial_df.iloc[0,0] = "not_nan"

for par_row in range(part_df_row_num):
    part_target = input_partial_df.iloc[par_row,0] # iterate the output_search_col column
    for ful_row in range(ful_df_row_num):
        full_target = input_full_df.iloc[ful_row,0] # full name file
        if search(part_target,full_target): # if two ACC match	
            input_partial_df.iloc[par_row,1] = input_full_df.iloc[ful_row,1]

# for par_col in range(3, part_df_col_num + 2): # the first cells are Nan, which causes error; two columns were added by the former command lines, thus the range of columns need to be enlarged (+2)
# 	ACC_target = input_partial_df.iloc[0, par_col] # the first row is ACC of genes
# 	for gene_row in range(gene_df_row_num):
# 		gene_target = input_gene_df.iloc[gene_row,0] # the first column is names of genes
# 		if search(ACC_target,gene_target):
# 			input_partial_df.iloc[0, par_col] = input_gene_df.iloc[gene_row,1] # replace ACC with gene names

input_partial_df.to_csv(output_fname, index_label = False, header = None)
            
    
