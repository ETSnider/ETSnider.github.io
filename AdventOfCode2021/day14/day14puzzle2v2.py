"""
Advent of Code 2021
Day 14 Challenge Part 2 v2

Task:
Your submarine must convert its hull to a stronger polymer. To do so, it offers a polymer template, and a series of insertion rules.
At each step, for each matching pair, an element is inserted between elements of the pair.
All pairings are considered simultaneously for each step, and added elements are not considered part of a pair until the next step.
Given a starting polymer, and a series of insertion rules, find the most and least common element after 40 steps, and their difference.


Notes: Had to abandon object-oriented approach due to heavy computational load. 
Switched to counting pairs, and replacing each number of a pair with an equal number of 
"""

def getInput():
	"""
	Reads the input from a file in the same directory.
	Output: a list, with element 0 being a string, element 1 being an empty string, and elements 2 onward being lists of form ['XY','Z'].
	"""
	with open("day14puzzle1input.txt",'r') as f:
		lines = f.readlines()
	data = [lines[0].strip()]
	for i in range(1,len(lines)):
		data.append(lines[i].strip().replace(" ","").split("->"))
	return data

def pairs(polymer):
	"""
	Converts a polymer string into a series of character pairs.
	Input: a string.
	Output: a list of strings of length 2.
	"""
	return [polymer[i:i+2] for i in range(len(polymer)-1)]
	
def replaceStep(polymer, rules):
	"""
	Applies the given rules to the input element pair dictionary.
	Input: a dict of pairs, and a dict of rules
	Output: a dict of pairs
	"""
	outpolymer = {**polymer}
	for pair in polymer.keys():
		outpolymer[pair] -= polymer[pair]
		if pair[0]+rules[pair] not in outpolymer:
			outpolymer[pair[0]+rules[pair]] = polymer[pair]
		else:
			outpolymer[pair[0]+rules[pair]] += polymer[pair]
		if rules[pair]+pair[1] not in outpolymer:
			outpolymer[rules[pair]+pair[1]] = polymer[pair]
		else:
			outpolymer[rules[pair]+pair[1]] += polymer[pair]
	return outpolymer
	
def countElem(lastElement,polymer):
	"""
	Counts the number of each element in a polymer, and outputs to console the most common element and its amount, the least common element and its amount, and the difference between the two as an integer.
	Input: a dict of character pairs.
	Output: the difference between the quantity of the most common element and the quantity of the least common element.
	"""
	count = {}
	for pair in polymer.keys():
		if pair[0] not in count:
			count[pair[0]] = polymer[pair]
		else:
			count[pair[0]] += polymer[pair]
	count[lastElement] += 1 ##Because the last element in the last pair is not duplicated.
	return max(count.values())-min(count.values())
	
	
	
def main():
	###First, read the input from a file.
	input = getInput()
	#print(input[0])
	###Next, use the input to build the polymer and rules dicts.
	formula = pairs(input[0])
	formulaDict = {formula[0]:1}
	for i in range(1,len(formula)): 
		if formula[i] not in formulaDict:
			formulaDict[formula[i]] = 1
		else:
			formulaDict[formula[i]] += 1
	#print(formulaDict)
	rules = dict(input[2:])
	#print(rules)
	###Then, iterate through the steps of replacement.
	for i in range(40):
		formulaDict = replaceStep(formulaDict,rules)
		print(i)
	###Count the elements, and output the difference between the most common and least common element's quantities.
	print(formulaDict)
	print(countElem(formula[-1][-1],formulaDict))
	
if __name__ == "__main__":
	main()