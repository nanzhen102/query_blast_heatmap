import pandas as pd

in_df = pd.read_csv('./2_multi_query/75cov_50aa_output.csv', header = [0,1], index_col = 0)

r_num, co_num = in_df.shape

genus_col = []

# insert a new column with the genus
for r in range(r_num):
    genus_cell = in_df.iloc[r,0].split(" ",1)[0]
    genus_col.append(genus_cell)

in_df.insert(0,"genus", genus_col, True)
in_df_grouped = in_df.groupby("genus")

in_df_grouped.sum().reset_index().to_csv('./2_multi_query/75cov_50aa_output_grouped.csv')

    