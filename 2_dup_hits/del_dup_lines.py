import pandas as pd
import numpy as np
from collections import defaultdict


in_f_name = "all_prot_query_screened_header_40ide_40cov.csv"
out_f_name = in_f_name.split(".")[0] + "_deduped.csv"

df = pd.read_csv(in_f_name, header = 0, index_col = None)

strain_seq_col = 1
query_col = 0

query_list = []
final_dup_drop_indices = []

row_num, col_num = df.shape  

# grouped = in_f_df.groupby('query acc.')
# grouped.to_frame().to_csv('grouped.csv')

group_start = None

# find a group in the first column

def get_index_positions(list_of_elems, element):
    ''' Returns the indexes of all occurrences of give element in
    the list- listOfElements '''
    index_pos_list = []
    index_pos = 0
    while True:
        try:
            # Search for item in list from indexPos to the end of list
            index_pos = list_of_elems.index(element, index_pos)
            # Add the index position in list
            index_pos_list.append(index_pos)
            index_pos += 1
        except:
            break
    print(index_pos_list)
    return index_pos_list

def list_duplicates(seq):
    tally = defaultdict(list)
    for i,item in enumerate(seq):
        tally[item].append(i)
    return ((key,locs) for key,locs in tally.items() if len(locs)>1)

# for row in range(row_num):
for row in range(200):

    if row > 0:
        if group_start == None:
            if df.iloc[row,0] == df.iloc[row-1,0]:
                group_start = row-1
        elif group_start != None:
            if df.iloc[row,0] != df.iloc[row-1,0]: ### Ending of a group detected
                group_len = row - group_start
                group_vals = df.iloc[group_start:row,1].values.tolist()

                all_dup_group_indices = []
                cur_indices_dups = []
                final_dup_group_indices = []
                trans_dup_indices = []
                
                print("Group Length: {}".format(group_len))
                
                for b in range(len(group_vals)):
                    cur_indices_dups = get_index_positions(group_vals,group_vals[b])
                    if len(cur_indices_dups) > 1:
                        all_dup_group_indices.append(cur_indices_dups[:])
                print("Messy list: {}".format(all_dup_group_indices))
                all_dup_group_indices = [item for sublist in all_dup_group_indices for item in sublist]
                
                print("Clean mess with duplicates: {}".format(all_dup_group_indices))

                for i in all_dup_group_indices:
                    if i not in final_dup_group_indices:
                        final_dup_group_indices.append(i)
                    
                print("Clean: {}".format(final_dup_group_indices))

                print("trans row num: {}".format(row))
                
                trans_dup_indices = [element + group_start for element in final_dup_group_indices]
                print(trans_dup_indices)
                
                final_dup_drop_indices.append(trans_dup_indices)
                
                group_start = None


final_dup_drop_indices = [item for sublist in final_dup_drop_indices for item in sublist]
print("Final duplicate drop list: {}".format(final_dup_drop_indices))
# df = df.reset_index(drop=True, inplace=True)

df = df.drop(final_dup_drop_indices)

### DELETE the selected indices here!!!
        
df.to_csv(out_f_name,index=False)


            

