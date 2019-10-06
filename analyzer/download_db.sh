wget ftp://ftp.ncbi.nlm.nih.gov/blast/db/FASTA/nr.gz -O reference/nr.gz
wget ftp://ftp.ensembl.org/pub/release-98/fasta/homo_sapiens/cdna/Homo_sapiens.GRCh38.cdna.all.fa.gz -O reference/Homo_sapiens.GRCh38.cdna.all.fa.gz
wget ftp://ftp.ensembl.org/pub/release-98/fasta/homo_sapiens/ncrna/Homo_sapiens.GRCh38.ncrna.fa.gz -O reference/Homo_sapiens.GRCh38.ncrna.fa.gz
cat reference/Homo_sapiens.GRCh38.cdna.all.fa.gz reference/Homo_sapiens.GRCh38.ncrna.fa.gz > reference/transcripts.fasta.gz
rm -f reference/Homo_sapiens.GRCh38.cdna.all.fa.gz reference/Homo_sapiens.GRCh38.ncrna.fa.gz