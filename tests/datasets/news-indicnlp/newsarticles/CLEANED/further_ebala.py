from barely_json import parse


filenames = ['ebala_articles']

for filestr in filenames:
	
	print('-'*20 + 'x' + '-'*20)
	print('Opening file {0} to be cleaned'.format(filestr))
	file1 = open(filestr + '.json')
	instr = file1.read()

	change = True

	outstr = ''
	for character in instr:

		newc = character

		if character == '\"':
			change = not change

		if change and character == '\'':
			newc = '\"'

#		if (not change) and character == '\"':
#			newc = '\''

		outstr += newc


	#print(outstr)

	file2 = open(filestr + '_cleaner.json', 'w')
	file2.write(outstr)
	print('written into {0}_cleaner.json'.format(filestr))

