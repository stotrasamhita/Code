import sys
import re

if len(sys.argv)==3:
	infile=sys.argv[1]
	outfile=sys.argv[2]
else:
	print 'Please Check the number of arguments'
	exit()

try:
	f = open(infile, 'r')
	s=[]
	for line in f:
		s.append(line)
except IOError:
	print infile+' does not exist in specified path'
	exit()
else:
	f.close()
	Shloka=str(' '.join(s))
	Shloka = re.sub('~N','G',Shloka)
	Shloka = re.sub('N\^','G',Shloka)
	Shloka = re.sub('~n','J',Shloka)
	Shloka = re.sub('R\^i','R',Shloka)
	Shloka = re.sub('uu','U',Shloka)
	Shloka = re.sub('ii','I',Shloka)
	Shloka = re.sub('aa','A',Shloka)
	Shloka = re.sub('ch','c',Shloka)
	Shloka = re.sub('e','E',Shloka)
	Shloka = re.sub('shh','S',Shloka)
	Shloka = re.sub('ksh','kS',Shloka)
	Shloka = re.sub('o','O',Shloka)
	Shloka = re.sub('j~n','jJ',Shloka)
	Shloka = re.sub('GY','jJ',Shloka)
	Shloka = re.sub('Sh','S',Shloka)
	Shloka = re.sub('sh','z',Shloka)
	Shloka = re.sub('\.\.\n','||\n</fourlineindentedshlokanum>\n<fourlineindentedshlokanum>\n',Shloka)
	Shloka = re.sub('\.\.','||',Shloka)
	Shloka = re.sub('\.h',' ',Shloka)
	Shloka = re.sub('\.n','M',Shloka)
	Shloka = re.sub(' \.\n','|\n',Shloka)
	Shloka = re.sub('\.',' ',Shloka)
	Shloka = re.sub('##','',Shloka)
	print Shloka
	print infile+' Parsed successfully'


try:
	o = open(outfile,'w')
except IOError:
	print outfile+' cannot be written'
else:
#for l in s:
	o.write(Shloka)
	o.close()
	print outfile+' written Successfully'