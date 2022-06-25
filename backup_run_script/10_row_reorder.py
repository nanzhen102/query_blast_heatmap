# -*- coding: utf-8 -*-

import pandas as pd
from re import search

in_fname = 'full_name_type_strain_DB_Jun21_2022_grouped.csv' # the csv file that needs to be recordered
# in_fname = "3.csv"
in_order_fname = "../y_order_plus_Periweissella.csv" # the csv file that contains the right order
out_fname = in_fname.split(".")[0]  + "_ordered.csv" # the output file

in_df = pd.read_csv(in_fname , header=None, index_col = 0) 
in_order_df = pd.read_csv(in_order_fname , header=0, index_col = False)

order_list = in_order_df.iloc[:,0].tolist()
# print(order_list)
out_df = in_df.reindex(order_list)

out_df.to_csv(out_fname, index_label = False, header = None)