from barely_json import parse

print('Opening file to be cleaned')
file1 = open('anandabazar_articles.txt')
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

file2 = open('anand.json', 'w')
file2.write(outstr)
print('written into anand.json')

