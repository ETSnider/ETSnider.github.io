"""
Advent of Code 2021
Day 7 Challenge Part 1

Task:
A number of crab submarines are attempting to line up. To move, they use an increasing amount of fuel, with the first step costing one, the second costing two, etc.
Given the positions of the crabs, find the position to line them up that uses the least fuel, and determine how much fuel that is.

Refactored to perform the fuel cost calculations more efficiently.
"""

def getCrabs():
	"""
	Reads a list of crab positions from a file in the same directory.
	Output: A list of integers.
	"""
	f = open("day7puzzle1input.txt",'r')
	line = f.readline()
	f.close()
	line = line.strip().split(',')
	crabs = []
	for num in line:
		crabs.append(int(num))
	return crabs
	
def findDiff(crabs,target,lastPos):
	"""
	Finds the sum of the fuel costs to move all crabs to a target position.
	Input: A list of integers of the crabs' positions, a target integer, and the furthest crab's position.
	Output: The sum of the fuel costs as an integer.
	"""
	positions = list(0 for x in range(lastPos + 1))
	for crab in crabs:
		positions[abs(crab-target)] += 1
	return costing(positions)
	
def costing(positions):
	"""
	Calculates the fuel cost to move a crab from its current position to the target position.
	Input: The number of crabs at each distance from the target position, as a list of integers.
	Output: The fuel cost as an integer.
	"""
	cost = 0
	tally = 0
	for num in range(len(positions)-1,-1,-1):
		tally += positions[num]
		cost += num * tally
	return cost
	
	
def main():
	###First, read the positions of the crabs from a file.
	crabs = getCrabs()
	###Next. find the farthest crab's position.
	lastPos = max(crabs)
	###Then, check each position for its fuel cost, and find the minimum.
	minFuel = findDiff(crabs,0,lastPos)
	minPos = 0
	for pos in range(1,lastPos+1):
		temp = findDiff(crabs,pos,lastPos)
		if temp < minFuel:
			minFuel = temp
			minPos = pos
	###Finally, output the minimum fuel cost and its position to the console.
	print(minPos)
	print(minFuel)
	
if __name__ == "__main__":
	main()