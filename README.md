# Query_Blast: package for query blast and the following analysis 

Written by Nanzhen and Eden.

## Dependency
- Python3 version >= 3.6.7

## Usage
Query_Blast is used to perform query blast and turn the output file into a proportion csv file.
``` bash
python main.py -i <txt_file_name>
```


## Files
 `full_name_Jan28_2022.csv`

 The file includes 337 type strains as well as the latest *Furfurilactobacillus* and *Weissella* strains.


---
- [ ] combine bash scripts
    ```bash
    # Paul's server
    # lab2-50 sever

    for f in *.fna; do prokka --kingdom Bacteria --force --outdir genomes_prokka_output --prefix ${f%.fna} --locustag ${f%.fna} $f; done # if the annotation is needed

    conda activate nanzhen_blast
    cat *.faa > all_prot.fasta # the database to blast against
    makeblastdb -in all_prot.fasta -out all_prot_database -dbtype prot
    tmux new -s name # depend on the file size, can skip this step
    blastp -db all_prot_database -query all_query.fasta -out all_prot_query.txt -outfmt "7 qacc sallacc pident qcovs evalue"


    ```
- [ ] combine R script / update all R scripts
- [ ] add variables for the cutoffs of csv filtering

Done:
- [ ] move output files into a new data folder
- [ ] update full_name.csv to full_name_Jan28_2022.csv
- [ ] match gene names - column
- [ ] FileExistsError: [Errno 17] File exists: 'output_result'


