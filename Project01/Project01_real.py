from Bio import SeqIO
from sys import argv
import os
script, fq_in, fq_out, min_q, min_length = argv
reads = SeqIO.parse(fq_in, "fastq")
trimmed_reads = SeqIO.parse("good_reads.fq", "fastq")
good_reads = []
final_reads = []


def read_trimmer():
    for record in reads:
        a = 0
        quality = record.letter_annotations['phred_quality']
        for i, q in enumerate(quality):
            if int(q) >= int(min_q):
                good_reads.append(record[a:])
                break
            else:
                a += 1
    SeqIO.write(good_reads, "good_reads.fq", "fastq")

def lenght_check():
    for record in trimmed_reads:
        if len(record.seq) >= int(min_length):
            final_reads.append(record)
    SeqIO.write(final_reads, fq_out, "fastq")


def main():
    read_trimmer()
    lenght_check()
    os.remove("good_reads.fq")
main()
