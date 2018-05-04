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
new_file = pd.read_table('Blast', header=None, names=names)
new_file_1 = new_file[["Query Accession",
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
         "Bitscore"]]
new_file_1.to_csv('Batch-results.txt', sep="\t) 
                                                          1,1           Top

