import os, shutil
# os.mkdir("output_result")

source_path = './'
dest_path = './output_result'

files = os.listdir(source_path)
for f in files:
	if f.startswith('all_prot_query_'):
		shutil.move(f, dest_path)

