#!/usr/bin/env nextflow 

/*
 * Define the pipeline parameters
 */
params.chunkSize = 5000
params.query = "./*.pep"
params.db = "/data/hort503_01_s18/example-data/swissprot"
params.out = "/top_hits_results.txt"

db_name = file(params.db).name
db_path = file(params.db).parent
fasta = file(params.query)
seq = Channel.from(fasta).splitFasta(by: params.chunkSize)
process blastp {

    input:
    file fasta from seq
    file db_path

    output:
    file 'blastp_result' into blastp_result
    file 'top_hits' into top_hits
    """
    blastp -db $db_path/$db_name -query $fasta -outfmt "6 qseqid nident qacc sacc sseqid pident length mismatch gapopen qstart qend sstart send evalue bitscore" > blastp_result
    cat blastp_result > top_hits
    """

}

process concat_blastp_hits {
    
    input:
    file 'top_hits' from top_hits

    output:
    file 'top_results' into top_results

    """
    cat top_hits > top_results
    python3 nextflow_python_wrangle.py
    """ 

}

process name_batch_blastp {

    input:
    file 'blastp_result' from blastp_result

    output:
    file 'Blast' into Blast

    """
    python3 nextflow_python_batch.py
    """

}
Blast.collectFile(name: params.out)
