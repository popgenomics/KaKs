#!/software/bin/python2.7

from Bio.SeqIO import parse
from os import listdir

path = "/scratch/cluster/monthly/croux/mercurialis/Bams/reads2snps/diploids/orf_fastas"

def consensus(x):
	cons = ""
	for i in range(len(x[0])): # loop over the sites 
		tmp = []
		for j in x: # loop over the sequences
			tmp.append(x[j][i])
		nBases = [tmp.count("A"), tmp.count("T"), tmp.count("C"), tmp.count("G")]
		if sum(nBases) == 0:
			cons += "N"
		else:
			cons += ["A", "T", "C", "G"][nBases.index(max(nBases))]
	return(cons)

listOfLoci = [ i for i in listdir(path) if "fas" in i ]

output = ""

for infile in listOfLoci:
	infile = path + "/" + infile
	input = parse(infile, "fasta")
	res = {}
	cnt = -1
	for i in input:
		if "huetti" not in i.id:
			cnt += 1
			res[cnt] = i.seq
	input.close()
	output += ">{0}\n{1}\n".format(infile.split(".")[0], consensus(res))

outfile = open(path + "/" + "consensus_annua_orf_geneCapture.fas", "w")
outfile.write(output)
outfile.close()


