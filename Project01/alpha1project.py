from Bio import SeqIO
from sys import argv
import numpy as np
generator = SeqIO.parse("SP1 copy.fq", "fastq")
def get_reads():
    for record in generator:
        print("%s %s %s" % (record.id, record.seq, record.letter_annotations["phred_quality"]))
get_reads()

def trim_read_front():
    handle = open("outfile", "w+")
    good_reads = {}

    with handle as f:
        i = 0
        for record in generator:
            base_checker()
            record =+ 1
            print("%s" % record)
            continue
        print(good_reads)
        SeqIO.write(good_reads, f, "fastq")
        #else:
            #i + 1
            #q =+ i
            #print("%i" % q)
            #continue
def base_checker():
    if record.letter_annotations["phred_quality"] in record >= 30:
        i = 0
        good_reads.append(record[i:])
        return()
    elif record.letter_annotations["phred_quality"[i:]] in record < 30:
        i =+ 1
        base_checker()
        return()
    else:
        if record.letter_annotations["phred_quality"[i:]] is None:
            exit()
trim_read_front()
