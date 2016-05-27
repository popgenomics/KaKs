#!/software/bin/python2.7
listOfPopulations = ["Antalya", "Barcelona", "Brouck", "Corinthe", "Paris", "Soton", "Tarragona", "Trabzon", "Villafranca", "Volos"]
listOfColumns = [2, 3, 4, 5, 6, 7, 8, 13, 14, 23, 24, 25, 26, 27, 28, 29]
listOfGenes = []
res = {}

for i in listOfPopulations:
	res[i] = {}
	infile = "output_" + i
	input = open(infile, "r")
	j = input.readline().strip().split("\t")
	header = ""
	for k in listOfColumns:
		header += "\t{0}_{1}".format(j[k], i)
	header += "\tdN_{0}\tdS_{0}\tdNdS_{0}\tpiNpiS_{0}".format(i)
	res[i]["header"] = header
	res[i]["stats"] = {}
	for j in input:
		j = j.strip().split("\t")
		stats = []
		if j[0] not in listOfGenes:
			listOfGenes.append(j[0]) # locus name
		for k in listOfColumns:
			stats.append(j[k])
		if float(j[13]) > 0:
			dN = str(float(j[7])/float(j[13]))
		if float(j[13]) <= 0:
			dN = "NA"
		if float(j[14]) > 0:
			dS = str(float(j[8])/float(j[14]))
		if float(j[14]) <= 0:
			dS = "NA"
		if dN != "NA" and dS != "NA" and float(dS) >0:
			dNdS = str(float(dN)/float(dS))
		if dN == "NA" or dS == "NA" or float(dS) <=0:
			dNdS = "NA"
		if float(j[26]) > 0 and float(j[27]) > 0:
			piNpiS = str(float(j[26])/float(j[27]))
		if float(j[26]) <= 0 and float(j[27]) <= 0:
			piNpiS = "NA"
		stats.append(dN)
		stats.append(dS)
		stats.append(dNdS)
		stats.append(piNpiS)
		res[i]["stats"][j[0]] = stats
	input.close()

res2 = "locus"
for i in listOfPopulations:
	res2 += "\t" + res[i]["header"]

res2 = res2.replace("\t\t", "\t")

res2 += "\n"

for i in listOfGenes:
	res2 += i + "\t"
	for j in listOfPopulations:
		if i not in res[j]["stats"]:
			res2 += "{0}".format("NA\t"*(len(listOfColumns)+4))
		if i in res[j]["stats"]:
			res2 += "\t".join(res[j]["stats"][i]) + "\t"
	res2 += "\n"

output = open("bilan_piNpiSdNdS.txt", "w")
output.write(res2)
output.close()


