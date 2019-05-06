from barely_json import parse


filenames = ['anandabazar_articles', 'ebala_articles', 'zeenews_articles']

for filestr in filenames:
	
	print('-'*20 + 'x' + '-'*20)
	print('Opening file {0} to be cleaned'.format(filestr))
	file1 = open('../' + filestr + '.txt')
	instr = file1.read()

	print('Starting the parse into dict')
	parsedict = parse(instr)
	print('Finished Parsing into the dict')

	c = 0
	outstr = '{\n'

	print('converting to JSONable format')
	for obj in parsedict['articles']:
		outstr += '\'art'+str(c)+'\': '
		outstr += str(obj)
		outstr += ','
		outstr += '\n'
		c += 1

	outstr += '\n}'

	file2 = open(filestr + '.json', 'w')
	file2.write(outstr)
	print('written into {0}.json'.format(filestr))

