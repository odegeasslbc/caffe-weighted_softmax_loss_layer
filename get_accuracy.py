import re,sys,os

log = open('log.txt')
res_g = open('res_g.txt','w')
res_a = open('res_a.txt','w')
res_s = open('res_s.txt','w')

itera = 0
for line in log:
	
	#if re.search(r'Testing net (#0)', line):
	#	new = re.search(r'\d+',line).group()+' '
	if re.search(r'Test net output #1: accuracy_genere', line):
		new=line[-9:]
		res_g.write(new)
		itera+=100
	if re.search(r'Test net output #0: accuracy_ar', line):
		new=line[-9:]
		res_a.write(new)
		itera+=100
	if re.search(r'Test net output #2: accuracy_st', line):
		new=line[-9:]
		res_s.write(new)
		itera+=100		

log.close()
res_g.close()
res_s.close()
res_a.close()
