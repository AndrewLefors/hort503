from Bio import SeqIO
trimmed = []
filtered = []
open_reads = SeqIO.parse("SP1 copy.fq", "fastq")
def trimmer():

    for record in open_reads:
        i = 0
        if record.letter_annotations["phred_quality"][i+2:] >= 30:
            filtered.append(record)
            return(trimmed)
        elif record.letter_annotations["phred_quality"][i:] < 30:
            i =+ 1
            trimmer()
            trimmed.append(record[i:])
        else:
            print("Trimming Complete!")

def trim_read_front():
    open("out_file", "w+")
    trimmer()
    return(trimmed)

pass_count = SeqIO.write(filtered, "out_file", "fastq")
print("%i reads passed quality check" % pass_count)
