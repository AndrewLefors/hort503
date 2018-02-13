from Bio import SeqIO
with open("SP1.fq", "rU") as handle:
    for record in SeqIO.parse(handle, "fastq"):
        print(record.id)
