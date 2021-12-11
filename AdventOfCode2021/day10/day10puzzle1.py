"""
Advent of Code 2021
Day 10 Challenge Part 1

Task: A navigation system is made out of chunks - pairs of brackets. 
Each line has one or more chunks, and each chunk can contain zero or more chunks.
Bracket pairs must match: {} [] () <>
Some chunks are corrupted, having a mismatcb of brackets.
Such corruptions have a syntax error score: for the first illegal character in each line, ) is 3, ] is 57, } is 1197, > is 25137.
Ignoring incomplete lines, find the total syntax error score for the lines.
"""

def main():
	###First, get the navigation system  from file.
	navigation = getNav()
	#print(navigation)
	###Next, find the unexpected bracket in each line.
	brackets = []
	for line in navigation:
		brackets.append(findCorrupt(line))
	###Then, find the syntax error score of the brackets.
	SES = countSyntaxErrorScore(brackets)
	print(SES)
	
def getNav():
	"""
	Reads the navigation system data from a file in the same directory.
	Output: A list of strings.
	"""
	#f = open("day10puzzle1testinput.txt",'r')
	f = open("day10puzzle1input.txt",'r')
	nav = f.readlines()
	f.close()
	for n in range(len(nav)):
		nav[n] = nav[n].strip('\n')
	return nav
	
def findCorrupt(line):
	"""
	Finds the first unexpected bracket in a line, if it exists, and returns it.
	Input: A String containing only bracket characters ( { [ < > ] } )
	Output: A closing bracket character, if an unexpected bracket is found, otherwise ''
	"""
	expected = []
	for bracket in line:
		if bracket ==  '(':
			print(bracket,end='')
			expected.append(')')
		elif bracket == '{':
			print(bracket,end='')
			expected.append('}')
		elif bracket == '[':
			print(bracket,end='')
			expected.append(']')
		elif bracket == '<':
			print(bracket,end='')
			expected.append('>')
		else:
			if expected[-1] == bracket:
				print(bracket,end='')
				expected.pop()
			else:
				print('',bracket)
				return bracket
	print('X')
	return 'X'
	
def countSyntaxErrorScore(bracketList):
	"""
	Calculates the syntax error score of the unexpected brackets.
	Input: A list of characters, ')' '}' ']' '>' ''.
	Output: An integer.
	"""
	print(bracketList)
	count, brack, curl, square, arrow = 0,0,0,0,0
	for bracket in bracketList:
		if bracket == ')':
			count += 3
			brack += 1
		elif bracket == '}':
			count += 1197
			curl += 1
		elif bracket == ']':
			square += 1
			count += 57
		elif bracket == '>':
			count += 25137
			arrow += 1
		else:
			continue
	print([brack,curl,square,arrow, 3*brack + 57*curl + 1197*square + 25137*arrow])
	return count
	
if __name__ == "__main__":
	main()