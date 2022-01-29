import pandas as pd

# group by genus name
def group(in_fname, out_fname): 
    in_df = pd.read_csv(in_fname, header = 0, index_col = 0)
    r_num, co_num = in_df.shape
    genus_col = []
    for r in range(r_num):
        genus_cell = str(in_df.iloc[r,1]).split(" ",1)[0]
        genus_col.append(genus_cell)

    in_df.insert(0,"genus", genus_col, True)
    in_df_grouped = in_df.groupby("genus")

    in_df_grouped.sum().reset_index().to_csv(out_fname)

# calculate the proportation of genes in each genus
def calcu(in_fname, out_fname): 
    input_tally_fname = in_fname
    output_fname = out_fname

    input_tally_df = pd.read_csv(input_tally_fname , header=None, index_col = 0) # open file with incomplete names
    row_num, col_num = input_tally_df.shape # rows - columns

    start_row = 1
    start_col = 1
    genus_count_col = 1

    for row in range(row_num):   
        if row >= 1: # 0行是基因编号，不计入计算
            denom = input_tally_df.iloc[row,genus_count_col] # what is the total number of strains 
            # print(denom) # save this line
            for col in range(col_num):
                if col >= start_col:
                    try:
                        input_tally_df.iloc[row,col] = int(int(input_tally_df.iloc[row,col])/int(denom) * 100)
                    except:
                        print("zero found")

    input_tally_df = input_tally_df.drop(input_tally_df.columns[1], axis = 1) # delete the column for calculation - all 1 and then sum up for each genus
    input_tally_df.to_csv(output_fname, index_label = False, header=None)

