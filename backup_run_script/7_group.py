import pandas as pd

in_df = pd.read_csv('all_prot_query_screened_header_40ide_70cov_positive_negative_species_gene_matched.csv', header = [0], index_col = 0)

r_num, co_num = in_df.shape

genus_col = []

# insert a new column with the genus
for r in range(r_num):
    genus_cell = in_df.iloc[r,1].split(" ",1)[0]
    genus_col.append(genus_cell)

in_df.insert(0,"genus", genus_col, True)
in_df_grouped = in_df.groupby("genus")

in_df_grouped.sum().reset_index().to_csv('all_prot_query_screened_header_40ide_70cov_positive_negative_species_gene_matched_grouped.csv')

    