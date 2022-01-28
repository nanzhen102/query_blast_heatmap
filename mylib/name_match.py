import pandas as pd
from re import search

def name_match(input_partial_fname, input_full_fname, output_fname):
    input_partial_df = pd.read_csv(input_partial_fname , header=None, index_col = False) # open pos_neg csv file
    input_full_df = pd.read_csv(input_full_fname , header=None, index_col = False) # open file with complete (full) names

    part_df_row_num, part_df_col_num = input_partial_df.shape # rows - columns 
    ful_df_row_num, ful_df_col_num = input_full_df.shape # rows - columns 
    input_partial_df.insert(loc=1, column="species", value="not_nan") # insert a column

    if pd.isna(input_partial_df.iloc[0,0]) == True: # in pos_neg csv, the first column of the first row is nan, thus need to fill a value
        input_partial_df.iloc[0,0] = "not_nan"

    for par_row in range(part_df_row_num):
        part_target = input_partial_df.iloc[par_row,0] # iterate the output_search_col column
        for ful_row in range(ful_df_row_num):
            full_target = input_full_df.iloc[ful_row,0] # full name file
            if search(part_target,full_target): # if two ACC match	
                input_partial_df.iloc[par_row,1] = input_full_df.iloc[ful_row,1]

    input_partial_df.to_csv(output_fname, index_label = False, header = None)
            
    
