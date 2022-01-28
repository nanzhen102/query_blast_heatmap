# -*-coding:utf-8 -*-
import pandas as pd
import numpy as np

input_file = pd.DataFrame(pd.read_csv("./2_multi_query/all_prot_query_screened_header.csv", header = 0))

# print(input_file.keys())

mask=((input_file["identity"]>=50) & (input_file["query coverage"]>= 75))

input_file=input_file.loc[mask] #还不知道为什么需要加这一句

input_file.to_csv("./2_multi_query/all_prot_query_screened_header_filter_75cov_50aa.csv", index = False) 