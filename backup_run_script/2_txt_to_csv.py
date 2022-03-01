# -*-coding:utf-8 -*-
import csv

with open ("all_prot_query_screened.txt", "r") as input:
  lines = input.readlines()
with open ("all_prot_query_screened.csv", "w") as output:
  spamwriter = csv.writer(output, dialect = 'excel')
  for line in lines:
    line_list = line.strip('\n').split('	')
    spamwriter.writerow(line_list)
input.close()
output.close()