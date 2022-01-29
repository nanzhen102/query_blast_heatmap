import py_compile
from mylib import pos_neg, species_name_match, prop_calcu
import sys, getopt, os, shutil

#!usr/bin/python

def main(argv):
    inputfile = ''
    try:
        opts,args = getopt.getopt(argv,"hi:o:",["ifile=","ofile="])
    except getopt.GetoptError:
        print('edit_txt.py -i <inputfile>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h': # get help
            print('edit_txt.py -i <inputfile>')
            sys.exit()
        elif opt in ("-i", "--ifile"): # run the py script
            inputfile = arg
    print('The input file is ' + inputfile)

# 1st module - pos_neg
    # first def
    output_del_line = inputfile.split('.')[0] + "_del_lin.txt"
    pos_neg.delete_lines(inputfile, output_del_line)

    # secod def
    output_to_csv = output_del_line.split('.')[0] + ".csv"
    pos_neg.txt_to_csv(output_del_line, output_to_csv)

    # third def
    output_head = output_to_csv.split('.')[0] + "_head.csv"
    pos_neg.header_add(output_to_csv, output_head)

    # fourth def
    # should add two vailables 
    output_fil = output_head.split(".")[0] + "_fil_75cov_50aa.csv"
    pos_neg.data_filter(output_head,output_fil)

    # fiveth def
    output_pos_neg = output_fil.split(".")[0] + "_pos_neg.csv"
    pos_neg.pos_neg(output_fil,output_pos_neg)

# 2nd module - name_match.py, 1st def
    in_full_fname = "full_name.csv"
    output_ful_name = output_pos_neg.split(".")[0] + "_fulname.csv"
    species_name_match.name_match(output_pos_neg, in_full_fname, output_ful_name)

# 3rd module - prop_calcu.py, 1st def
    output_grouped = output_ful_name.split(".")[0] + "_grouped.csv"
    prop_calcu.group(output_ful_name, output_grouped)

# 3rd module - prop_calcu.py, 2nd def
    output_cal = output_grouped.split(".")[0] + "_cal.csv"
    prop_calcu.calcu(output_grouped, output_cal)    

if __name__ == "__main__":
    main(sys.argv[1:])


# move output files into another folder
os.mkdir("output_result")
source_path = './'
dest_path = './output_result'

files = os.listdir(source_path) # get all file names
for f in files:
	if f.startswith('all_prot_query_'):
		shutil.move(f, dest_path)
