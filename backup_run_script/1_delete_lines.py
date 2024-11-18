# 删除注释行，即#开始的行。且不留空行

with open ("/Users/nanzhen/Documents/1_phd_2020/5_doctoral_program/0.6_metabolism_taxonomy_202405/7_fig1_6/fig3_update_v6/query_blast_combine.txt", "r") as input:
  lines = input.readlines()
with open ("all_prot_query_screened.txt", "w") as output:
  for line in lines:
    if '#' in line:
      line = line.replace(".", "")
    else:
      output.write(line)
input.close()
output.close()