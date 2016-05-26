#!/usr/bin/python
#script that produces input (fasta+gff) files from reads2snps
from Bio.SeqIO import parse

infile = "/scratch/cluster/monthly/croux/guillaume/CDS_annua_huetii_cleaned.fas"

input = parse(infile, "fasta")

alignement = {}
gff = {}

for i in input:
	gene = i.id.split("|")[0]
	if gene not in alignement:
		alignement[gene] = ""
	if gene not in gff:
		gff[gene] = "Mercurialis\t.\tCDS\t1\t{0}\t.\t+\t.\tID={1}\n".format(len(i.seq), gene)
	alignement[gene] += ">{0}\n{1}\n".format(i.id, i.seq)
input.close()

for i in alignement:
	infile = "/scratch/cluster/monthly/croux/guillaume/manva/" + i + ".fas"
	input = open(infile, "w")
	input.write(alignement[i])
	input.close()
	infile = "/scratch/cluster/monthly/croux/guillaume/manva/" + i + ".gff"
	input = open(infile, "w")
	input.write(gff[i])
	input.close()

