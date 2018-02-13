from Bio import SeqIO
from sys import argv
import os
script, fq_in, fq_out, min_q, min_length = argv
reads = SeqIO.parse(fq_in, "fastq")
trimmed_reads = SeqIO.parse("tmp", "fastq")
good_reads = []
final_reads = []
def get_read():
    for record in reads:
        print(record)

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
    SeqIO.write(good_reads, "tmp", "fastq")

def lenght_check():
    passed = 0
    reject = 0
    for record in trimmed_reads:
        if len(record.seq) >= int(min_length):
            final_reads.append(record)
            passed += 1
        else:
            reject += 1
    SeqIO.write(final_reads, fq_out, "fastq")
    print("%i Reads were found\n%i Reads were removed\n%i Reads were trimmed and kept" % ((passed + reject), reject, passed))

def main():
    print("Reading File...")
    #get_read()
    read_trimmer()
    print("Trimming File...")
    lenght_check()
    os.remove("tmp")
    print("Done.")
main()
