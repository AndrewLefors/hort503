from Bio import SeqIO
import numpy as np
from sys import argv
script, input_file, output_file, form, min_q, min_size = argv

fq_in = input_file
fq_out = output_file
file_type = form
quality = min_q
length = min_size
open_input = open(input_file)
generator = SeqIO.parse(open_input, f"{form}")
close_outbound = open_input.close()
def get_read(fq_in):
    for index, record in enumerate(generator):
        print("read %i\n ID = %s\n Sequence %s\n Quality Score: \n%s"
              % (index, record.id, record.seq, record.letter_annotations["phred_quality"]))

#get_read(input_file)



def trim_read_front(fq_in, quality, length):
    trimmed_reads = [ ]
    with open(f"{fq_out}", "w+") as out_file:
        for index, record in enumerate(trimmed_reads):
            q_score = record.letter_annotations["phred_quality"]
            i = 0
            count = 0
            for index, score in enumerate(q_score):
                if i in score >= int(f"{quality}"):
                    #base =+ 1 ##Testing to see if I can find any low quality read
                    trimmed_reads.append(record.sequence)
                    index =+ 1
                elif score[i:] < int(f"{quality}"):
                     count =+1
                     i =+ 1
                else:
                    SeqIO.write(trimmed_reads, f"{fq_out}", "fastq")
                    open_input.close()
                    print("Trimmed %i reads" % count)
                    print("Retained %i reads" % index)

#trim_read_front(fq_in, quality, length)
def main():

    #open_outbound = open(f"{fq_out}", "w+")
    #close_outbound = open_outbound.close()
    #get_read(fq_in)
    trim_read_front(fq_in, quality, length)


main()
