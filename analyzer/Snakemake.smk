rule quality_trim:
        input:
                '{sample}_1.fastq',
                '{sample}_2.fastq'
        output:
                '{sample}_1_val_1.fq',
                '{sample}_2_val_2.fq'
        shell:
                'trim_galore --quality 20 --fastqc --length 50 --trim-n --cores 5 --paired {input}'

rule host_clean:
        input:
                'dbs/reference_cdna_ncrna_ensembl',
                '{sample}_1_val_1.fq',
                '{sample}_2_val_2.fq'
        output:
                'kallisto',
                fq1='{sample}_R1.notaligned.fq',
                fq2='{sample}_R2.notaligned.fq'
        run:
                shell('kallisto quant -o {output} --pseudobam -t 5 -i {input}')
                shell('samtools view -f 13 {output}/pseudoalignments.bam | bamToFastq -i /dev/stdin -fq {output.fq1} -fq2 {output.fq2}')


rule protein_clean:
        input:
                db='dbs/uniref50'
                read1='{sample}_R1.notaligned.fq',
                read2='{sample}_R2.notaligned.fq'
        output:
                out1='{sample}_R1.notaligned.diamond',
                out1un='{sample}_R1.notaligned.diamond.un.fq',
                out1al='{sample}_R1.notaligned.diamond.al.fq',
                out2='{sample}_R2.notaligned.diamond',
                out2un='{sample}_R2.notaligned.diamond.un.fq',
                out2al='{sample}_R2.notaligned.diamond.al.fq'
        run:
                shell('diamond blastx -d {db} -p 5 -q {input.read1} -a {output.out1} -k 1 --un {out1un} --al {out1al} --unfmt fastq --alfmt fastq')
                shell('diamond blastx -d {db} -p 5 -q {input.read2} -a {output.out2} -k 1 --un {out1un} --al {out1al} --unfmt fastq --alfmt fastq')