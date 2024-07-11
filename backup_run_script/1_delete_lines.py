# 删除注释行，即#开始的行。且不留空行

with open ("inlA_query_blast.txt", "r") as input:
  lines = input.readlines()
with open ("all_prot_query_screened.txt", "w") as output:
  for line in lines:
    if '#' in line:
      line = line.replace(".", "")
    else:
      output.write(line)
input.close()
output.close()