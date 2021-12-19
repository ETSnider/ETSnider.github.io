"""
Advent of Code 2021
Day 18 Challenge 2

Task: You must help a snailfish with his math homework.
Each snailfish number is an ordered pair, and each element can be an integer or another pair.
To add 2 snailfish numbers, make a snailfish number with each pair as an element, ie [x1,y1] + [x2,y2] = [[x1,x2],[x2,y2]]
However, snailfish numbers must be reduced.
	If any pair is nested inside 4 pairs, the left most of such pairs explodes.
	If any regular number is 10 or greater, it splits.
	When neither applies, the number is reduced. 
	After encountering one action, return to the top of the list.
	
To explode a pair:
	The pair's left value is added to the first regular number to the left of the exploding pair.
	The pair's right value is added to the first regular number to the right of the exploding pair.
	Then, the exploding pair is replaced by a 0.
	
To split a number:
	The number becomes a pair, with the left element equal to the number divided by 2 rounded down, and the right number equal to the number divided by 2 rounded up.
	
Then, the magnitude of a snailfish number is equal to 3 times the magnitude of the left element plus 2 times the magnitude of the right element.
Given a list of snailfish numbers, what is the largest magnitude of the sum of two numbers on the list?
"""
import sys
sys.setrecursionlimit(10**6)
from math import floor, ceil

def getInput():
	with open("day18puzzle1input.txt",'r') as f:
		lines = f.read()
	snailNums = tuple(lines.splitlines())
	return snailNums

class Node:
	def __init__(self, val):
		self.value = val
	
	def __repr__(self):
		return f"{self.value}"
	
	def __eq__(self,other):
		return True if type(other)==Node and self.value == other.value else False
		
	def __hash__(self):
		return hash(self.value)

flatten=lambda l: sum(map(flatten,l),[]) if type(l) == tuple else [l]
	
def to_AST(ast):
	#print(ast)
	if type(ast) == int:
		return Node(ast)
	left,right = ast
	return (to_AST(left),to_AST(right))
	
def explodeAST(ast):
	#print("Checking for explosions")
	flat = flatten(ast)
	#print(flat)
	i = 0
	explosion = False
	#print(ast[0])
	#print(ast[1])
	def explode(ast,flat,depth=0):
		nonlocal i, explosion
		if type(ast) == Node:
			i += 1
			return ast 
		#print(ast)
		left, right = ast[0],ast[1]
		if type(left)==Node and type(right) == Node:
			if depth>3 and not explosion:
				if i > 0:
					flat[i-1].value += flat[i].value
				if i + 1< len(flat) - 1:
					flat[i+2].value += flat[i+1].value
				explosion = True
				return Node(0)
		return (explode(left,flat,depth+1),explode(right,flat,depth+1))
	return explode(ast,flat)
	
def splitAST(ast):
	halved = False
	def halve(ast):
		nonlocal halved
		if type(ast) == Node:
			if not halved and ast.value>9:
				halved = True
				return (Node(floor(ast.value/2)),Node(ceil(ast.value/2)))
			return ast
		left, right = ast[0],ast[1]
		return (halve(left),halve(right))
	return halve(ast)
		
def getMagnitude(ast):
	if isinstance(ast,Node):
		return ast.value
	left, right = ast
	return 3*getMagnitude(left) + 2*getMagnitude(right)
	
def addSnailNums(ast1,ast2):
	snailNum = (ast1,ast2)
	actionFlag = True
	#print(snailNum)
	while(actionFlag):
		actionFlag = False
		old = snailNum
		new = explodeAST(snailNum)
		#print(new)
		if old != new:
			#print("exploding")
			#print(new)
			actionFlag = True
			snailNum = new
			continue
		new = splitAST(snailNum)
		#print(new)
		if old != new:
			#print("splitting")
			#print(new)
			actionFlag = True
			snailNum = new
	#print(snailNum)
	return snailNum
		
def main():
	snailNums = getInput()
	#print(snailSum)
	#print(len(snailNums))
	maxSum = 0
	for xnum in range(len(snailNums)):
		for ynum in [ num for num in range(len(snailNums)) if num!=xnum]:
			snailSum = addSnailNums(to_AST(eval(snailNums[xnum])),to_AST(eval(snailNums[ynum])))
			mag = getMagnitude(snailSum)
			if mag > maxSum:
				maxSum = mag
			#print(snailSum)
	#print(getMagnitude(snailSum))
	print(maxSum)
	
if __name__ == "__main__":
	main()