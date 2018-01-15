print("Do you need to Index your reference Genome?", end=' ')
index = input
print("Do you want to Align your Reads to the Indexed Reference Genome?")
align = input()
print("Do you want to convert your SAM file to BAM format?")
bam = input()
print(f"""
Do you want to Index your reference? {index}
Do you want to Align your reads? {align}
Do you want to convert your SAM files to BAM format? {bam}

""")
