"""
Advent of Code 2021
Day 10 Challenge Part 2

Task: A navigation system is made out of chunks - pairs of brackets. 
Each line has one or more chunks, and each chunk can contain zero or more chunks.
Bracket pairs must match: {} [] () <>
Some chunks are corrupted, having a mismatcb of brackets.
Such corruptions have a syntax error score: for the first illegal character in each line, ) is 3, ] is 57, } is 1197, > is 25137.
Some chunks are incomplete, missing closing brackets.
For these chunks, their syntax error score starts at zero, and then, for each bracket auto-completed, score is first multiplied by 5 then 1 is added for ), 2 is added for ], 3 is added for ), and 4 is added for >.
Only the median auto-completion score is taken from all lines.
Find the total syntax error score of the navigation system.
"""

def main():
###First, get the navigation system  from file.
	navigation = getNav()
	#print(navigation)
	###Next, find the unexpected bracket in each line, or its auto-completion score.
	brackets = []
	for line in navigation:
		brackets.append(findCorruptIncomplete(line))
	print(brackets)
	###Then, find the syntax error score of the brackets.
	SES = countSyntaxErrorScore([brack for brack in brackets if brack in [')',']','}','>']])
	###Find the median of the auto-completion scores.
	completed = list([closer for closer in brackets if closer not in [')',']','}','>']])
	print(completed)
	completionScore = findMedian(completed)
	###Add the two scores and output the sum to the console.
	print([SES,completionScore,SES+completionScore])
	
def findMedian(nums):
	scores = sorted(nums)
	print(scores)
	numlen = len(scores)
	if numlen%2 == 0:
		out = (scores[numlen//2]+scores[1+numlen//2])/2
	else:
		out = scores[numlen//2]
	return out
	
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
	
def findCorruptIncomplete(line):
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
	complete = {')':1,']':2,'}':3,'>':4}
	print('X',end='\t')
	score = 0
	for bracknum in range(len(expected)):
		closer = expected[-(bracknum+1)]
		print(closer,end='')
		score *= 5
		score += complete[closer]
	print(score)
	return score
	
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