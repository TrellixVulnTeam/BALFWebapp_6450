from modules import sheetoperator, nonetodash, lastday
from functools import reduce
import time

def exec(individualsnf=sheetoperator.individualsnf, individualsf=sheetoperator.individualsf, individualspet=sheetoperator.individualspet, individualsgr=sheetoperator.individualsgr, equipsnf=sheetoperator.equipsnf, equipsf=sheetoperator.equipsf):
	header = ''
	podium = []


	# HEADER CONTROL
	with open(r"modules/templates/eqnf/headertemplate.html", 'r') as fp:
		header = fp.read() 

	with open('templates/eqnf.html', 'w') as f:
		f.write(header)

	# HEADER CONTROL


	# PODIUM CONTROL

	# Read the podium template
	with open(r"modules/templates/eqnf/podiumtemplate.html", 'r') as fp:
		podium = fp.readlines()

	# Changing the dummy text
	with open(r"workfile.html", 'w') as fp:
		for number, line in enumerate(podium):
			if number not in [1, 4, 6, 9, 12, 17, 38, 41, 44, 47, 50, 53]: #Lines that the code will delete
				fp.write(line)

	# Edit with a loop
	i = 0
	while i <=2:
		eqnfindex = int(individualsnf[0] + individualsf[0] + individualspet[0] + individualsgr[0] + i+1)
		with open("workfile.html", "r") as readingfile:
			rcontents = readingfile.readlines()
		rcontents.insert(1, str(f'"{i+1}"'))
		rcontents.insert(4, f'<img class="badge podiumelement" src="../static/badges/badge{i+1}.png">')
		rcontents.insert(6, str(nonetodash.nonetodash(sheetoperator.tot[eqnfindex][1])))
		rcontents.insert(9, str(nonetodash.nonetodash(sheetoperator.tot[eqnfindex][7])))
		rcontents.insert(12, str(nonetodash.nonetodash(sheetoperator.tot[eqnfindex][lastday.fetchlastday()])))
		rcontents.insert(17, f'"t{i+1}"')
		rcontents.insert(38, str(nonetodash.nonetodash(sheetoperator.tot[eqnfindex][2])))
		rcontents.insert(41, str(nonetodash.nonetodash(sheetoperator.tot[eqnfindex][3])))
		rcontents.insert(44, str(nonetodash.nonetodash(sheetoperator.tot[eqnfindex][4])))
		rcontents.insert(47, str(nonetodash.nonetodash(sheetoperator.tot[eqnfindex][5])))
		rcontents.insert(50, str(nonetodash.nonetodash(sheetoperator.tot[eqnfindex][6])))
		rcontents.insert(53, str(nonetodash.nonetodash(sheetoperator.tot[eqnfindex][8])))
		write(rcontents)
		i += 1
	# PODOIUM CONTROL

	# LIST CONTROL
	with open(r"modules/templates/eqnf/listtemplate.html", 'r') as fp:
		list = fp.readlines()

	# Changing the dummy text
	with open(r"workfile.html", 'w') as fp:
		for number, line in enumerate(list):
			if number not in [1, 7, 11, 15, 19, 25, 46, 49, 52, 55, 58, 61]: #Lines that the code will delete
				fp.write(line)

	# Edit with a loop
	i = 3
	while i <= sheetoperator.equipsnf[0]-1:
		eqnfindex = int(individualsnf[0] + individualsf[0] + individualspet[0] + individualsgr[0] + i+1)
		with open("workfile.html", "r") as readingfile:
			rcontents = readingfile.readlines()
		rcontents.insert(1, str(f'"{i+1}"'))
		rcontents.insert(7, str(f'{i+1}'))
		rcontents.insert(11, str(nonetodash.nonetodash(sheetoperator.tot[eqnfindex][1])))
		rcontents.insert(15, str(nonetodash.nonetodash(sheetoperator.tot[eqnfindex][7])))
		rcontents.insert(19, str(nonetodash.nonetodash(sheetoperator.tot[eqnfindex][lastday.fetchlastday()])))
		rcontents.insert(25, f'"t{i+1}"')
		rcontents.insert(46, str(nonetodash.nonetodash(sheetoperator.tot[eqnfindex][2])))
		rcontents.insert(49, str(nonetodash.nonetodash(sheetoperator.tot[eqnfindex][3])))
		rcontents.insert(52, str(nonetodash.nonetodash(sheetoperator.tot[eqnfindex][4])))
		rcontents.insert(55, str(nonetodash.nonetodash(sheetoperator.tot[eqnfindex][5])))
		rcontents.insert(58, str(nonetodash.nonetodash(sheetoperator.tot[eqnfindex][6])))
		rcontents.insert(61, str(nonetodash.nonetodash(sheetoperator.tot[eqnfindex][8])))
		write(rcontents)
		print (i)
		i += 1
	# LIST CONTROL

	# FOOTER CONTROL
	with open(r"modules/templates/eqnf/footertemplate.html", 'r') as fp:
		footer = fp.read() 

	with open('templates/eqnf.html', 'a') as f:
		f.write(footer)
	# FOOTER CONTROL
		
# Final step: save and to the list we go
def write(rcontents):
	with open("templates/eqnf.html", "a") as f:
		rcontents = "".join(rcontents)
		f.write(rcontents)