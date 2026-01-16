import csv
import pandas as pd

input_text_file = "/Users/nanzhen/Documents/1_phd_2020/5_doctoral_program/0.12_Furfuri_new_species_202505/16_revise_20251103/4_tree_32gen_names/enzyme/query_blast.txt"  # Original input file
final_csv_file = "all_prot_query_screened_header.csv"  # Final output file

def remove_lines_with_hash_and_convert_to_csv(input_file, output_file, headers):
    """Removes lines containing the # symbol, converts to CSV, and adds headers."""
    rows = []
    with open(input_file, "r") as infile:
        for line in infile:
            if "#" not in line:
                rows.append(line.strip('\n').split('\t'))

    data = pd.DataFrame(rows, columns=headers)
    data.to_csv(output_file, index=False)

# Headers to add
headers = ['query acc.', 'strain accs.', 'identity', 'query coverage', 'evalue']

# Execute the processing
remove_lines_with_hash_and_convert_to_csv(input_text_file, final_csv_file, headers)

print("Processing complete. Final output:", final_csv_file)
