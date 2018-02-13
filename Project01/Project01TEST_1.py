import numpy
from Bio import SeqIO
from sys import argv
script, input_file, output_file, min_q, min_size = argv
generator = SeqIO.parse(input_file, 'fastq')
#def get_read(fq):
#    print(f"Openining {fq}")
#    open(fq, 'r+')
#    count = 0
#    for sequence in generator:
#        count =+ 1
#        print(sequence, sequence.letter_annotations["phred_quality"])

#    print("%i reads" % count)
quality = int(min_q)
size = min_size
fq_input = input_file
#get_read(fq_input)
fq_out = output_file


def trim_read_front(fq, q_score, length):
    output = open("fq_out", "w+")
    trimmed_reads = []
    for sequence in generator:
        base_score = sequence.letter_annotations['phred_quality']
        count = 0
        for i, q in enumerate(base_score):
            if q < q_score:
                count += 1
                if count == 1:
                    break
            elif q >= int(q_score):
                count = 0
                trimmed_reads.append(i)
        if count != 1:
            print(q_score)
        else:
            print(f"{sequence.annotations} is below the threshold, will not be included in results")
    print(trimmed_reads)
    #output.writelines(trimmed_reads)
#Quality read will filter out all reads below the threshold, set by the user.
    #quality_read = []
    #for sequence in generator:
    #    if len(sequence.seq) >= int(min_size):
    #        quality_read.append(record)
    #print("%i reads retained." % len(quality_read))
    #SeqIO.write(quality_read, f"Trimmed{fq}", "fastq")

trim_read_front(fq_input, quality, size)
