"""
Advent of Code 2021
Day 8 Challenge Part 2

Task: Wires are connected to segments of seven-segment displays randomly. 
A system produces 10 wire signal combinations trying to render the numbers, producing 4 segment-side signals as valid numbers.
Decode these signals, and find the sum of all the output values.
"""

def getInput():
	"""
	Reads the input data from a file in the same directory.
	Output: A list of strings of form "word word word word word word word word word word | word word word word"
	"""
	f=open("day8puzzle1input.txt",'r')
	lines = f.readlines()
	f.close()
	return lines

def main():
	###First, read the input from a file.
	lines = getInput()
	###Next, decode each panel, and sum the displayed numbers together.
	count = 0
	for line in lines:
		count += decodePanel(line)
	###Then, output this sum to the console.
	print(count)
	
	
def decodePanel(line):
	"""
	Decodes a line of wire signals to a 7-segment panel.
	Input: A string in the form "word word word word word word word word word word | word word word word"
	Output: The combined four numbers of the 7-segment panel, as an integer
	"""
	###Separate the wire-side signals and the light-side signals.
	line = line.split('|')
	wireSig = line[0].strip().split()
	lightSig = line[1].strip().split()
	###Declare lists to store which wire-side signals result in each given light-side number.
	one = []
	two = []
	three = []
	four = []
	five = []
	six = []
	seven = []
	eight = []
	nine = []
	zero = []
	
	###Freebie numbers with unique signal lengths: 1, 4, 7, 8
	for wsig in wireSig:
		print(wsig)
		siglen = len(wsig)
		if siglen == 2:
			for i in range(2):
				if wsig[i] not in one: one.append(wsig[i])
		elif siglen == 4:
			for i in range(4):
				if wsig[i] not in four: four.append(wsig[i])
		elif siglen == 3:
			for i in range(3):
				if wsig[i] not in seven: seven.append(wsig[i])
		elif siglen == 7:
			#print(wsig)
			for i in range(7):
				#print(i)
				#print(wsig[i])
				if wsig[i] not in eight: eight.append(wsig[i])
		else:
			continue

	###Numbers with signal length 6: 0,6,9
	for wsig in wireSig:
		if len(wsig)==6:
			print(wsig)
			if one[0] not in wsig or one[1] not in wsig:
				for i in range(6):
					if wsig[i] not in six: six.append(wsig[i])
			elif four[0] not in wsig or four[1] not in wsig or four[2] not in wsig or four[3] not in wsig:
				for i in range(6):
					if wsig[i] not in zero: zero.append(wsig[i])
			else:
				for i in range(6):
					if wsig[i] not in nine: nine.append(wsig[i])
		else:
			continue
	###Numbers with signal length 5: 2,3,5
	for wSig in wireSig:
		if len(wSig)==5: 
			if wSig[0] not in nine or wSig[1] not in nine or wSig[2] not in nine or wSig[3] not in nine or wSig[4] not in nine:
				for i in range(5):
					if wSig[i] not in two: two.append(wSig[i])
			elif one[0] not in wSig or one[1] not in wSig:
				for i in range(5):
					if wSig[i] not in five: five.append(wSig[i])
			else:
				for i in range(5):
					if wSig[i] not in three: three.append(wSig[i])
		else:
			continue
	print([zero,one,two,three,four,five,six,seven,eight,nine])

	"""
	##logic to get each segment, no longer necessary
	asig = list(x for x in seven if x not in one)[0]			
	csig = one[0] if one[0] not in six else one[1]
	fsig = list(x for x in one if x!=csig)[0]
	dsig = list(x for x in eight if x not in zero)[0]
	bsig = list(x for x in four if x not in one and x!=dsig)[0]
	gsig = list(x for x in nine if x not in four and x!=asig)[0]
	esig = list(x for x in zero if x not in nine)[0]
	"""
	###unscramble numbers
	cypher = [zero, one, two, three, four, five, six, seven, eight, nine]
	outnum = ['','','','']
	for i in range(4):
		for j in range(10):
			if sorted(cypher[j]) == sorted(lightSig[i]):
				outnum[i] = str(j)
				break
	outnum = "".join(outnum)
	outnum = int(outnum)
	return outnum
	
	
		
	

if __name__ == "__main__":
	main()