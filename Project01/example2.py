from Bio import SeqIO
good_reads = (rec for rec in \
              SeqIO.parse("SP1 copy.fq", "fastq") \
              if rec.letter_annotations["phred_quality"] > 30
reads = SeqIO.write(good_reads, "good_quality.fastq", "fastq")
print("Saved %i reads" % reads)
