"""
Advent of Code 2021
Day 14 Challenge Part 2

Task:
Your submarine must convert its hull to a stronger polymer. To do so, it offers a polymer template, and a series of insertion rules.
At each step, for each matching pair, an element is inserted between elements of the pair.
All pairings are considered simultaneously for each step, and added elements are not considered part of a pair until the next step.
Given a starting polymer, and a series of insertion rules, find the most and least common element after 40 steps, and their difference.

Note: left for reference, refactored in "day14puzzle2v2.py".
"""

def getInput():
	"""
	Reads the input from a file in the same directory.
	Output: a list, with element 0 being a string, element 1 being an empty string, and elements 2 onward being lists of form ['XY','Z'].
	"""
	with open("day14puzzle1input.txt",'r') as f:
		lines = f.readlines()
	data = []
	for line in lines:
		data.append(line.strip().replace(" ","").split("->"))
	return data

class Element:
	"""
	Represents an element.
	Attributes:
	value: the element label as a string
	active: whether the element is considered in the current step, default False.
	"""
	def __init__(self, val):
		self.value = val
		self.active = False
		
class Polymer:
	"""
	Represents a list of elements.
	Attributes:
	chain: a list of Element objects
	Methods:
	getNext(int index): returns the value of the next active element after the index, or -1 if none are active.
	"""
	def __init__(self, polyList):
		self.chain = []
		for elem in polyList:
			self.chain.append(Element(elem))
			self.chain[-1].active = True
	
	def getNext(self, index):
		while(index < len(self.chain)-1):
			#print(index)
			#print(self.chain[index].value,self.chain[index].active)
			if self.chain[index+1].active:
				return self.chain[index+1].value
			elif index < len(self.chain) - 2:
				index += 1
		return -1
			
	def __repr__(self):
		outstring = ""
		for elem in self.chain:
			outstring += elem.value
		return outstring
	
def replaceStep(polymer, rules):
	"""
	Applies the given rules to the input Polymer.
	Input: a Polymer object, and a list of lists of rules of form ['XY','Z']
	Output: a Polymer object
	"""
	for rule in rules:
		i = 0
		while (polymer.getNext(i) != -1):
			if polymer.chain[i].active == True and polymer.chain[i].value==rule[0][0] and polymer.getNext(i) == rule[0][1]:
				polymer.chain.insert(i+1,Element(rule[1]))
			i += 1
	for i in range(len(polymer.chain)):	
		polymer.chain[i].active = True
	return polymer
	
def countElem(polymer):
	"""
	Counts the number of each element in a Polymer object, and outputs to console the most common element and its amount, the least common element and its amount, and the difference between the two as an integer.
	Input: a Polymer object
	"""
	elements = []
	count = []
	for elem in polymer.chain:
		if elem.value in elements:
			count[elements.index(elem.value)] += 1
		else:
			elements.append(elem.value)
			count.append(1)
	most = [elements[count.index(max(count))],max(count)]
	least = [elements[count.index(min(count))],min(count)]
	print(most)
	print(least)
	print(most[1]-least[1])
	
def main():
	###First, read the input from a file.
	input = getInput()
	###Next, use the input to build the Polymer and rules list.
	formula = Polymer(list(char for char in input[0][0]))
	#print(formula)
	rules = input[2:]
	#print(rules)
	###Then, iterate through the steps of replacement.
	for i in range(40):
		formula = replaceStep(formula,rules)
		#print(formula)
	###Count the elements, and output the difference between the most common and least common element's quantities.
	countElem(formula)
	
if __name__ == "__main__":
	main()