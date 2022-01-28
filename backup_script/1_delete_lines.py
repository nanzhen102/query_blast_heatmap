# 删除注释行，即#开始的行。且不留空行

with open ("csv", "r") as input:
  lines = input.readlines()
with open ("output_fname", "w") as output:
  for line in lines:
    if '#' in line:
      line = line.replace(".", "")
    else:
      output.write(line)
input.close()
output.close()