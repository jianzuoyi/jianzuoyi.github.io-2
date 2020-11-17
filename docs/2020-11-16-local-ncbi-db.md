一文搞懂NCBI Blast本地数据库（NT/NR等）构建

## 背景介绍

blast+：   [ftp://ftp.ncbi.nlm.nih.gov/blast/executables/LATEST](ftp://ftp.ncbi.nlm.nih.gov/blast/executables/LATEST)

blast db：[ftp://ftp.ncbi.nlm.nih.gov/blast/db](ftp://ftp.ncbi.nlm.nih.gov/blast/db)

README：[ftp://ftp.ncbi.nlm.nih.gov/blast/db/README](ftp://ftp.ncbi.nlm.nih.gov/blast/db/README)

通过查看README，我们知道nt和nr库的内容：nr是蛋白库（非冗余的），nt是核酸库（部分非冗余的）。

| File Name | Content Description                                          |
| --------- | ------------------------------------------------------------ |
| nr.gz*    | non-redundant protein sequence database with entries from GenPept, Swissprot, PIR, PDF, PDB, and RefSeq. |
| nt.gz*    | nucleotide sequence database, with entries from all traditional divisions of GenBank, EMBL, and DDBJ; excluding bulk divisions (gss, sts, pat, est, htg) and wgs entries. Partially non-redundant. |

## 下载blast库

 BLAST+程序包中提供了一个脚本`update_blastdb.pl`可以方便地下载blast数据库。

首先用以下命令查看有哪些数据库可供下载：

```bash
perl update_blastdb.pl --showall
```

> 16S_ribosomal_RNA
> 18S_fungal_sequences
> 28S_fungal_sequences
> Betacoronavirus
> ITS_RefSeq_Fungi
> ITS_eukaryote_sequences
> LSU_eukaryote_rRNA
> LSU_prokaryote_rRNA
> SSU_eukaryote_rRNA
> cdd_delta
> env_nr
> env_nt
> human_genome
> landmark
> mouse_genome
> nr
> nt
> pataa
> patnt
> pdbaa
> pdbnt
> ref_euk_rep_genomes
> ref_prok_rep_genomes
> ref_viroids_rep_genomes
> ref_viruses_rep_genomes
> refseq_protein
> refseq_rna
> refseq_select_prot
> refseq_select_rna
> swissprot
> taxdb
> tsa_nr
> tsa_nt

如要下载nt库，用以下命令：

```bash
nohup perl update_blastdb.pl --decompress nt &> update.log &
```

后台下载并自动解压，如果中途断网，重启下载支持断点续传，很方便。

可惜的是，如果网速不好，80多GB的压缩文件，很难下载下来，最好用我们之前介绍过的Aspera软件高速下载，其安装方法见之前文章：[Aspera：基因组数据高速下载利器，以NCBI和EBI数据下载为例](https://zhuanlan.zhihu.com/p/245450890)



Aspera下载nt库：

```bash
ascp -i ~/.aspera/connect/etc/asperaweb_id_dsa.openssh -l 100M -k 1 -T anonftp@ftp.ncbi.nlm.nih.gov:/blast/db/FASTA/nt.gz ./
```



下载完毕，构建数据库索引：

```bash
makeblastdb -dbtype nucl -in nt.fa -out nt.fa
```



## 测试

准备查询文件：test.fa

```bash
>chr1
CGATAATTCATCTGGCCGCCTTCCACACCCAGCGCGCGCAAAAAGTGGTGGCGGAAACGATCCGCACTGAAAATACCGTGGAGATAGGTTCCCATGATACGACCATCGGGC
```

测试命令：

```bash
time blastn -query test.fa -db /path/to/nt.fa -num_threads 48 -max_target_seqs 5 -outfmt 6
```

结果如下：

```bash
chr1    CP046720.1      100.000 111     0       0       1       111     1286985 1287095 1.92e-49        206
chr1    CP044338.1      100.000 111     0       0       1       111     1283638 1283748 1.92e-49        206
chr1    MK355143.1      100.000 111     0       0       1       111     76      186     1.92e-49        206
chr1    MK355138.1      100.000 111     0       0       1       111     76      186     1.92e-49        206
chr1    MK355136.1      100.000 111     0       0       1       111     76      186     1.92e-49        206

real    0m15.609s
user    1m17.647s
sys     0m31.350s
```

本地NT库构建成功。

