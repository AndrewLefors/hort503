from Bio import SeqIO
from sys import argv
import numpy as np
generator = SeqIO.parse("SP1 copy.fq", "fastq")
out_put = open("out_file", "w+")
good_reads = []
i = 0
q = 0
passed = 0
failed = 0
def mini_trim():
    for i, q in enumerate(score):
        if q >= 30:
            i =+ 1
            passed =+ 1
            SeqIO.write(record[i:], out_put, "fastq")
        elif q < 30:
            q =+ 1
            mini_trim()
def trimmer():
    for record in SeqIO.parse("SP1 copy.fq", "fastq"):
        score = record.letter_annotations['phred_quality']
        mini_trim()
trimmer()
print("%i Passed Quality check" % passed)
