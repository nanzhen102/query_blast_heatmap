import py_compile
from mylib import pos_neg
import sys, getopt

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

if __name__ == "__main__":
    main(sys.argv[1:])


