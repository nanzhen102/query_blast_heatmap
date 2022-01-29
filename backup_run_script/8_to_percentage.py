# -*- coding: utf-8 -*-

import pandas as pd

#%%
input_tally_fname = './2_multi_query/75cov_50aa_output_grouped.csv'
output_fname = './2_multi_query/75cov_50aa_output_grouped_with_proportion.csv'

input_tally_df = pd.read_csv(input_tally_fname , header=None) # open file with incomplete names

row_num, col_num = input_tally_df.shape # rows - columns

start_row = 2
start_col = 3
genus_count_col = 2


# input_tally_df.iloc[3,2]

#%%

for row in range(row_num):   
    if row >= 2:
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
            
    
