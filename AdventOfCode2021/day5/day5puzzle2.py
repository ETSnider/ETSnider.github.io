import io
import numpy as np
"""
Advent of Code 2021:
Day 5 Challenge Part 1

Task: 
A series of hydrothermal vents form lines on a grid. Determine all points where lines overlap.
"""
def getLines():
	"""
	Reads line coordinates from a file in the same directory, and parses them into pairs of points
	Line format: "x1,y1 ->  x2,y2"
	Output: a 3d list of integers, of size 1000x2x2
	"""
	f = open("day5puzzle1input.txt",'r')
	lines = f.readlines()
	f.close()
	temp = [0,0]
	for linenum in range(len(lines)):
		lines[linenum] = lines[linenum].split(" -> ")
		for pointnum in range(2):
			lines[linenum][pointnum] = lines[linenum][pointnum].strip().split(',')
			temp[0] = int(lines[linenum][pointnum][0])
			temp[1] = int(lines[linenum][pointnum][1])
			lines[linenum][pointnum] = temp[:]
		#print(line)
	return lines

def main():
	###First, read the lines from a file, and parse the pairs of points
	grid = np.zeros((1000,1000),dtype=int)
	
	inLines = getLines()
	#print(inLines)
	###Map the lines on the grid by representing each point as the number of lines passing through it.
	####A seperate process is used for horizontal lines, vertical lines, and each direction of diagonal lines, to achieve the same result.
	for line in inLines:
		if line[0][0] == line[1][0]:
			xCoord = line[0][0]
			low = min(line[0][1],line[1][1])
			high = max(line[0][1],line[1][1])
			for j in range(low,high + 1):
				grid[xCoord][j] += 1
		elif line[0][1] == line[1][1]:
			yCoord = line[0][1]
			low = min(line[0][0],line[1][0])
			high = max(line[0][0],line[1][0])
			for i in range(low,high + 1):
				grid[i][yCoord] += 1
		else:
			if line[0][0]<line[1][0] and line[0][1]<line[1][1]:
				for i in range(line[1][0] - line[0][0] + 1):
					grid[line[0][0]+i][line[0][1]+i] += 1
			elif line[0][0]<line[1][0] and line[0][1]>line[1][1]:
				for i in range(line[1][0] - line[0][0] + 1):
					grid[line[0][0]+i][line[0][1]-i] += 1
			elif line[0][0]>line[1][0] and line[0][1]<line[1][1]:
				for i in range(line[0][0] - line[1][0] + 1):
					grid[line[0][0]-i][line[0][1]+i] += 1
			else:
				for i in range(line[0][0] - line[1][0] + 1):
					grid[line[0][0]-i][line[0][1]-i] += 1
	###Iterate over all points on the grid, record which points have more than one line passing through them, and tally them.
	outPoints=[]
	intersections = 0
	for i in range(1000):
		for j in range(1000):
			#print(grid[i][j],end=' ')
			if grid[i][j] > 1:
				outPoints.append([i,j])
				intersections += 1

					
	#print(outPoints)
	###Output the tally of points with more than one line passing through them to the console.
	print(intersections)
	#print(len(outPoints))

if __name__ == "__main__":
	main()