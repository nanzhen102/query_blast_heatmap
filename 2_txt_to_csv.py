# -*-coding:utf-8 -*-
import csv

with open ("./2_multi_query/all_prot_query_screened.txt", "r") as input:
  lines = input.readlines()
with open ("./2_multi_query/all_prot_query_screened.csv", "w") as output:
  spamwriter = csv.writer(output, dialect = 'excel')
for line in lines:
  line_list = line.strip('\n').split('	')
  spamwriter.writerow(line_list)
input.close()
output.close()