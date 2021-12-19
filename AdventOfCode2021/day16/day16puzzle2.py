"""
Advent of Code 2021
Day 16 Challenge Part 2

Task:
You have received a transmission, which has been saved in hexadecimal format. Ignore trailing 0s.
Each packet starts with a header: the first three bits encode the packet version, and the next 3 encode the packet type ID, bigendian.
For packets of type 4, a single binary number is encoded: it is padded with 0s until its length is a multiple of 4, then it is divided
	into groups of 4 bits, with the ending group being prefixed by 0 and the others prefixed by 1.
Other packet types are operator packets. The bit after the packet header is the length type ID.
	If it is 0, the next 15 bits are a number that represents the total length in bits of the subpackets contained by this packet.
	If it is 1. the next 11 bits are a number that represents the number of subpackets contained by this packet.
	After the length type ID and the 15 or 11 bit number, the subpackets appear:
		3 bits version number, 3 bits type ID, etc.
		
Find the sum of the version numbers of all the packets.		
"""

def getInput():
	"""
	Reads the input from a file, and converts the bytes to a sequence of bits.
	Output: a string.
	"""
	with open("day16puzzle1input.txt",'r') as f:
		packet = f.read()
	bytearray = []
	byteDict = {'0':'0000','1':'0001','2':'0010','3':'0011','4':'0100','5':'0101','6':'0110','7':'0111','8':'1000','9':'1001','A':'1010','B':'1011','C':'1100','D':'1101','E':'1110','F':'1111'}
	for char in packet:
		bytearray.append(byteDict[char])
	return "".join(bytearray)

def product(numList):
	"""
	Finds the product of a list.
	Input: a list of integers
	Output: an integer
	"""
	outNum = 1
	for num in numList:
		outNum *= num
	return outNum

def greater(numList):
	"""
	Determines if the first element of a list is greater than the second.
	Input: a list of integers
	Output: 0 or 1
	"""
	return 1 if numList[0]>numList[1] else 0
	
def lesser(numList):
	"""
	Determines if the first element of a list is lesser than the second.
	Input: a list of integers
	Output: 0 or 1
	"""
	return 1 if numList[0]<numList[1] else 0
	
def same(numList):
	"""
	Determines if the first element of a list is equal to the second.
	Input: a list of integers
	Output: 0 or 1
	"""
	return 1 if numList[0]==numList[1] else 0

	
def evalPacket(signal):
	"""
	Parses the packets in the signal, and sums their version numbers.
	Input: a string.
	Output: the sum of version numbers as an integer, and the read position in the signal as an integer.
	"""
	print(signal)
	versionNum = int(signal[0:3],2)
	print(versionNum)
	print()
	typeID = signal[3:6]
	readPosition = 6
	operations = {'000':sum,'001':product,'010':min,'011':max,'101':greater,'110':lesser,'111':same}
	subpacketLiterals = []
	if typeID == '100':
		readByte = signal[readPosition:readPosition+5]
		literal = readByte[1:]
		endFlag = readByte[0]
		readPosition += 5
		while endFlag!='0':
			readByte = signal[readPosition:readPosition+5]
			readPosition += 5
			literal += readByte[1:]
			endFlag = readByte[0]
		
		literal = int(literal,2)
		return literal,readPosition
	elif signal[readPosition] == '0':
		subpacketsLen = int(signal[readPosition+1:readPosition+16],2)
		padding = subpacketsLen%4
		readPosition += 16
		tempa,tempb = evalPacket(signal[readPosition:readPosition+subpacketsLen])
		subpacketLiterals.append(tempa)
		readPosition += tempb
		#print(tempa,tempb,subpacketsLen)
		while(tempb < subpacketsLen):
			subpacketsLen -= tempb
			tempa, tempb = evalPacket(signal[readPosition:readPosition+subpacketsLen])
			subpacketLiterals.append(tempa)
			readPosition += tempb
		
		return operations[typeID](subpacketLiterals[:]), readPosition
	elif signal[readPosition] == '1':
		numSubpackets = int(signal[readPosition+1:readPosition+12],2)
		#print(numSubpackets)
		readPosition += 12
		for subpacket in range(numSubpackets):
			tempa,tempb = evalPacket(signal[readPosition:])
			subpacketLiterals.append(tempa)
			readPosition += tempb
			
		return operations[typeID](subpacketLiterals[:]), readPosition
	else:
		return operations[typeID](subpacketLiterals[:]), readPosition + readPosition%4

def main():
	###First, read and parse the input signal from file.
	signal = getInput()
	###Next, find the sum of the version numbers of the packets.
	outnum, readPosition = evalPacket(signal)
	###Output the sum of the version numbers to the console
	print(outnum)

if __name__ =="__main__":
	main()