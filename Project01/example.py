good_reads = (rec for rec in \
              SeqIO.parse("SP1 copy.fq", "fastq") \
              if min(rec.letter_annotations["phred_quality"]) >= 30
count = SeqIO.write(good_reads, "good_quality.fastq", "fastq")
print("Saved %i reads" % count)
