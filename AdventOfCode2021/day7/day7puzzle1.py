"""
Advent of Code 2021
Day 7 Challenge Part 1

Task:
A number of crab submarines are attempting to line up. To move one space, they must use one unit of fuel.
Given the positions of the crabs, find the position to line them up that uses the least fuel, and determine how much fuel that is.
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
	
def findDiff(crabs,position):
	"""
	Finds the sum of the differences in position between a list of crabs and a target position.
	Input: A list of integers of the crabs' positions, and a target integer.
	Output: The sum of the differences as an integer.
	"""
	sum = 0
	for crab in crabs:
		sum += abs(crab - position)
	return sum
	
def main():
	###First, read the positions of the crabs from a file.
	crabs = getCrabs()
	###Next. find the farthest crab's position.
	lastPos = max(crabs)
	###Then, check each position for its fuel cost, and find the minimum.
	minFuel = findDiff(crabs,0)
	minPos = 0
	for pos in range(1,lastPos+1):
		temp = findDiff(crabs,pos)
		if temp < minFuel:
			minFuel = temp
			minPos = pos
	###Finally, output the minimum fuel cost and its position to the console.
	print(minPos)
	print(minFuel)
	
if __name__ == "__main__":
	main()