import numpy as np
import pandas as pd
names = ["Query ID",
         "Number of Matches",
         "Query Accession",
         "Subject Accession",
         "Subject Title",
         "Percent Identity",
         "Alignment Length",
         "Number of Mismatches",
         "Number of Gap Openings",
         "Start of Alignment Query",
         "End of Alignment Query",
         "Start of Alignment Subject",
         "End of Alignment Subject",
         "Expect Value",
         "Bitscore"]
##Take File from blast-nextflow output and drop all columns except qseqid and nident
new_file = pd.read_table('top_results', header=None, names=names)
new_file_1 = new_file[["Query ID","Number of Matches"]]

#Sort the File for top hits first by setting ascending=False in the sort method
new_file_2 = new_file_1.sort_values(by=["Number of Matches"], ascending=False)

#Save the file in tab-delimited format
new_file_2.to_csv('Blast-Protein hits.txt', sep="\t")
