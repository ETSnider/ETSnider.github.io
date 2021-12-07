import io
import itertools
"""
Advent of Code 2021:
Day 6 Challenge Part 2

Task: 
A population of anglerfish spawn every 7 days. 
Once an anglerfish is born, it needs an extra 2 days before it can start having offspring of its own.
Assuming the anglerfish do not die, what will their population be after 256 days?
Input:
A list of the ages of the current anglerfish population, on a single line, seperated by ','.

Major Challenge: Memory Usage
"""
def main():
	###First, fetch the ages of the current population of anglerfish, and sort them by age.
	curr_population = getInput()
	#print(curr_population)
	next_population = []
	###Increases the age of the anglerfish population by 256
	for i in range(256):
		next_population = newDay(curr_population)
		curr_population = next_population
		#print(list(curr_population))
	###Sums the final population of the anglerfish, and prints the result to the console.
	print(sum(curr_population))

def getInput():
	"""
	Reads the anglerfish ages from a file in the same directory, and sorts them by age.
	Returns a list of integers of length 9.
	"""
	f = open("day6puzzle1input.txt",'r')
	line = f.readline()
	f.close()
	line = line.strip().split(',')
	line = (int(x) for x in line)
	bins=[0,0,0,0,0,0,0,0,0]
	for fish in line:
		bins[fish]+=1
	return bins

def newDay(curr_population):
	"""
	Ages each anglerfish by a day. Shifts bins to the left, and adds bin 0 fish to bin 6 and their spawn to bin 8
	Input: a list of integers of length 9.
	Output: a list of integers of length 9.
	"""
	temp = curr_population[0]
	for age in range(1,9):
		curr_population[age-1] = curr_population[age]
	curr_population[6] += temp
	curr_population[8] = temp
	return curr_population

if __name__ == "__main__":
	main()