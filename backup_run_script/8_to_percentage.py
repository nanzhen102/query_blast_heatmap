# -*- coding: utf-8 -*-

import pandas as pd

#%%
input_tally_fname = 'all_prot_query_screened_header_40ide_70cov_positive_negative_species_gene_matched_grouped.csv'
output_fname = 'all_prot_query_screened_header_40ide_70cov_positive_negative_species_matched_grouped_with_proportion.csv'

input_tally_df = pd.read_csv(input_tally_fname , header=None) # open file with incomplete names

row_num, col_num = input_tally_df.shape # rows - columns

start_row = 1
start_col = 3
genus_count_col = 2


# input_tally_df.iloc[3,2]

#%%

for row in range(row_num):   
    if row >= 1:
        denom = input_tally_df.iloc[row,genus_count_col] # what is the total number of strains 
        print(denom)
        for col in range(col_num):
            if col >= start_col:
                try:
                    input_tally_df.iloc[row,col] = int(input_tally_df.iloc[row,col])/int(denom) * 100
                except:
                    print("zero found")


#%%
input_tally_df.to_csv(output_fname, index_label = False)
            
    
