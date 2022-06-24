# -*- coding: utf-8 -*-

import pandas as pd
from re import search

in_fname = '1.csv' # the csv file that needs to be recordered
in_order_fname = "2.csv" # the csv file that contains the right order
out_fname = in_fname.split(".")[0]  + "_ordered.csv" # the output file

in_df = pd.read_csv(in_fname , header=0, index_col = 0) 
in_order_df = pd.read_csv(in_order_fname , header=0, index_col = False)

order_list = in_order_df.iloc[:,0].tolist()
out_df = in_df.reindex(order_list)

out_df.to_csv(out_fname, index_label = False, header = None)