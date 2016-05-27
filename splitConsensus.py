#!/software/bin/python2.7
from Bio.SeqIO import parse

infile = "/scratch/cluster/monthly/croux/mercurialis/Bams/reads2snps/diploids/orf_fastas/consensus_annua_orf_geneCapture.fas"

input = parse(infile, "fasta")

cnt1 = 0
cnt2 = 0
res = ""
for i in input:
	cnt1 += 1
	res += ">{0}\n{1}\n".format(i.id, i.seq)
	if cnt1%100 == 0:
		cnt2 += 1
		output = open("input_blast_{0}.fas".format(str(cnt2)), "w")
		output.write(res)
		output.close()
		res = ""
		cnt1 = 0
cnt2 += 1
output = open("input_blast_{0}.fas".format(str(cnt2)), "w")
output.write(res)
output.close()

