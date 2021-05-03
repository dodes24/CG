\# CG
Cancer Genomics Data Analysis Exercise

First index the Human reference genome using BWA

```console
bwa index GCA_000001405.28_GRCh38.p13_genomic.fna.gz
```
Align and create sam file
```console
bwa mem GCA_000001405.28_GRCh38.p13_genomic.fna.gz tu.r1.fq.gz tu.r2.fq.gz > tumor.sam
bwa mem GCA_000001405.28_GRCh38.p13_genomic.fna.gz tu.r1.fq.gz tu.r2.fq.gz > wt.sam
```
Convert sam to bam
```console
samtools view -O BAM -o tumor.bam tumor.sam
samtools view -O BAM -o wt.bam wt.sam
```
Sort and index the BAM file
```console
samtools sort -T temp -O bam -o tumor.sorted.bam tumor.bam
samtools sort -T temp -O bam -o wt.sorted.bam wt.bam
```
Index sorted bam files
```console
samtools index tumor.sorted.bam
samtools index wt.sorted.bam
```
Remove duplicates from PCR
```console
samtools rmdup -r -S tumor.sorted.subset.bam tumor.deduplicate.bam
samtools rmdup -r -S wt.sorted.subset.bam wt.deduplicate.bam
```
Identify the depth at each locus from a bam file
```console
samtools depth tumor.deduplicated.bam > tumor.deduplicated.coverage
samtools depth wt.deduplicated.bam > wt.deduplicated.coverage
```
Extract just chromosomeX = CM000685
```console
grep "CM000685" tumor.deduplicated.coverage > tumor.chrx.coverage
grep "CM000685" wt.deduplicated.coverage > wt.chrx.coverage
```

Subset to the region of interest
```console
sed -n '/20000000/,/40000000/p' tumor.chrx.coverage > tumor.extract
sed -n '/20000000/,/40000000/p' wt.chrx.coverage > wt.extract
```











