"""
Advent of Code 2021
Day 8 Challenge Part 1

Task: Wires are connected to segments of seven-segment displays randomly. 
A system produces 10 wire signal combinations trying to render the numbers, producing 4 segment-side signals as valid numbers.

Given a record of these combinations and outcomes, count the number of instances of the digits 1, 4, 7, or 8.
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
	###Next, count the number of 1s, 4s, 7s or 8s in each line, and add them together.
	count = 0
	for line in lines:
		count += count1478(line)
	###Then, output this count to the console.
	print(count)
	
	
def count1478(line):
	"""
	Analyzes the segment-side signals of wire-side signal segment-side signal combination, and counts the number of 1s, 4s, 7s and 8s.
	Input: A string of form "word word word word word word word word word word | word word word word".
	Output: An integer.
	"""
	line=line.split("|")[1]
	line=line.strip().split()
	count = 0
	for word in line:
		if len(word) in [2,3,4,7]:
			count += 1
	return count

if __name__ == "__main__":
	main()