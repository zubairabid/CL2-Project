from barely_json import parse


filenames = ['anandabazar_articles_clean', 'ebala_articles_cleaner', 'zeenews_articles']

for filestr in filenames:
	
	print('-'*20 + 'x' + '-'*20)
	print('Opening file {0} to count. Ignore for now if zeenews'.format(filestr))
	file1 = open(filestr + '.json')
	instr = file1.read()

	lines = []
	c = 0 
	for word in instr.split():

		if 'art' in word and word.startswith('\"art'):
#			print(word)
#			print('art'+str(c))
#			print()
			if ('art'+str(c)) not in word:
				lines.append(c)
				c += 1

			c += 1


	print('Missing lines are:' + str(lines))

