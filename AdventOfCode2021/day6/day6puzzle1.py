import io
import itertools
"""
Advent of Code 2021:
Day 6 Challenge Part 1

Task: 
A population of anglerfish spawn every 7 days. 
Once an anglerfish is born, it needs an extra 2 days before it can start having offspring of its own.
Assuming the anglerfish do not die, what will their population be after 80 days?
Input:
A list of the ages of the current anglerfish population, on a single line, seperated by ','.

Major Challenge: Memory Usage
Using lists resulted in a memory error, so the functions were refactored to use generator functions and yields.
"""
def main():
	###First, read the population from file
	curr_population = getInput()
	#print(curr_population)
	next_population = []
	###Increases the age of the anglerfish population by 80.
	for i in range(80):
		next_population = newDay(curr_population)
		curr_population = next_population
		#print(list(curr_population))
	###Counts the number of anglerfish in the current generation, and prints it to the console.
	print(len(list(curr_population)))

def getInput():
	"""
	Reads a list of anglerfish ages from a file in the same directory, and returns them as a generator function.
	Output: A generator function of integers.
	"""
	f = open("day6puzzle1input.txt",'r')
	line = f.readline()
	f.close()
	line = line.strip().split(',')
	line = (int(x) for x in line)
	return line

def newDay(curr_population):
	"""
	Ages each anglerfish by a day. Iterates through the input population, and decreases time to next spawn by one.
	If the time to next spawn would be less than 0, it is changed to 6, and a new anglerfish is added.
	Input: A generator function of integers.
	Output: A generator function of integers.
	"""
	for fish in curr_population:
		#print(fish)
		if fish == 0:
			yield 6
			yield 8
		else:
			yield fish-1

if __name__ == "__main__":
	main()