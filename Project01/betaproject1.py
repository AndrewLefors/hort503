from Bio import SeqIO
trimseq=[]
good_reads=[]
for rec in SeqIO.parse('SP1 copy.fq', 'fastq'):
    read_quals = rec.letter_annotations['phred_quality']
    count = 0
    for i, q in enumerate(read_quals):
        if q <= 20:
            count += 1
            if count == 1:
                break
        elif count:
            count = 0
    if count != 1:
        trimseq.append(rec)
    else:
        trimseq.append(rec[i-1:])
    for i, q in enumerate(trimseq):
        if len(q) >= 30:
            good_reads.append(i)



#print("Saved %s reads") % len(trimseq)
output_handle=open("out_put", "w")
SeqIO.write(good_reads, output_handle, "fastq")
output_handle.close()
