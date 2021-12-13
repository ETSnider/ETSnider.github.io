"""
Advent of Code 2021
Day 11 Challenge Part 2

Task: An array of octopi have flashing lights. Each octopus has an energy level from 0 to 9, and when it reaches 9, it flashes, and resets to 0.
When an octopus flashes, it increases the energy level of the 8 octopi surrounding it by 1, which may cause them to flash.
An octopus can only flash once per step.
The energy level of each octopus increases by 1 each step.
Given an array of octopi, find the first step where every octopus flashes.
"""
	
class Octopus:
	"""
	A representative of an octopus and its state.
	Attributes:
		level: an integer between 0 and 9
		flashed: a flag to show whether the octopus has reached max level this step
	"""
	def __init__(self,inEnergy):
		self.level = inEnergy
		self.flashed = False
	
	def __repr__(self):
		return str(self.level)
		
class OctoArray:
	"""
	Storage for the array of octopi and associated functions
	Attributes:
		flashCount: a running count of all the flashes that occur
		grid: a 2d array of Octopus objects, generated from the input file in the same directory
	Methods:
		Step(): increases the step of the grid of octopi
		Flash(int xCoord, int yCoord): applies the flash effect about the octopus at the given coordinates
	"""
	def __init__(self):
		self.flashCount = 0
		self.grid = [[]]
		with open("day11puzzle1input.txt",'r') as f:
			input = f.readlines()
		for lineNum in range(len(input)):
			if lineNum != 0: self.grid.append([])
			for num in list(x for x in input[lineNum] if x != '\n'):
				self.grid[lineNum].append(Octopus(int(num)))
				
	def __repr__(self):
		outstring = ""
		for line in self.grid:
			outstring +="\n"
			for oct in line:
				outstring +=f"{oct.level} "
		return outstring + "\n"
		
	def Step(self):
		"""
		Advances the array by one step.
		"""
		###First, increase the energy of each octopus by 1 for time increase
		for width in range(len(self.grid[0])):
			for height in range(len(self.grid)):
				self.grid[width][height].level +=1
		###Apply all flashes.
		flashCheck = True
		while(flashCheck):
			flashCheck = False
			for width in range(len(self.grid[0])):
				for height in range(len(self.grid)):
					if self.grid[width][height].level > 9 and self.grid[width][height].flashed == False:
						flashCheck = True
						self.Flash(width,height)
		###Reset flags
		for width in range(len(self.grid[0])):
			for height in range(len(self.grid)):
				if self.grid[width][height].flashed == True:
					self.grid[width][height].level = 0
					self.grid[width][height].flashed = False
				
					
	def Flash(self,width,height):
		"""
		Causes an octopus to flash.
		Input: The horizontal and vertical positions of the octopus, as integers.
		"""
		###Set flashed flag so it cannot flash again
		self.grid[width][height].flashed = True
		###Increase flash count
		self.flashCount += 1
		###Check if the octopus is on an edge or in a corner
		wide = [-1,0,1]
		if width == 0:
			wide = [0,1]
		elif width == len(self.grid[0]) - 1:
			wide = [-1,0]
		tall = [-1,0,1]
		if height == 0:
			tall = [0,1]
		elif height == len(self.grid) - 1:
			tall = [-1,0]
		###Increase the energy of surrounding octopi	
		for i in wide:
			for j in tall:
				if self.grid[width + i][height + j].flashed == False and self.grid[width + i][height + j].level <= 9:
					self.grid[width + i][height + j].level += 1
		
	def checkSync(self):
		for line in self.grid:
			for oct in line:
				if oct.level != 0:
					return False
		return True



def main():
	###First, create the grid of octopi
	octolist = OctoArray()
	#print(octolist)
	###Next, iterate through steps until the flashes synchronise
	stepNum = 0
	while(not octolist.checkSync()):
		stepNum += 1
		octolist.Step()
	#print(octolist)
	###Then output the step count to the console
	print(stepNum)
	

if __name__ == "__main__":
	main()					