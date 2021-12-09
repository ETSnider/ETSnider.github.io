"""
Advent of Code 2021
Day 9 Challenge Part 1

Task: The lava tube you are in is filling with smoke. Only the low points of the cave are safe.
A point is s low point if it is lower than the points above, below, left and right of it.
Each low point has a risk level which is its height plus 1.
Given a map of the heights of the lava tube, find the sum of the risk levels of all the low points.
"""

def main():
	###First, read the cave height map from file.
	cave = getCave()
	###Next, find the low points in the cave.
	lowPoints = getLow(cave)
	###Then, sum the risk values of these low points.
	riskLevel = getRisks(cave,lowPoints)
	###Finally, output the sum of risk levels to the console.
	print(riskLevel)


def getCave():
	"""
	Reads the heights of the points of the cave from a file in the same directory.
	Output: n lines of m digits, as a list of strings.
	"""
	f = open("day9puzzle1input.txt",'r')
	lines = f.readlines()
	f.close()
	return list(x.strip() for x in lines)
	
def getLow(cave):
	"""
	Passes through each point in the cave and returns a list of all points that are lower than its horizontal and vertical neighbours.
	Input: n lines of m digits, as a list of strings.
	Output: a list of lists of coordinates. Format: [[x0,y0],[x1,y1],[x2,y2]...]
	"""
	lowPoints = []
	for row in range(len(cave)):
		for point in range(len(cave[row])):
			#print([row,point])
			if row > 0 and int(cave[row-1][point]) <= int(cave[row][point]):
				continue
			if row < len(cave)-1 and int(cave[row+1][point]) <= int(cave[row][point]):
				continue
			if point > 0 and int(cave[row][point-1]) <= int(cave[row][point]):
				continue
			if point < len(cave[row])-1 and int(cave[row][point+1]) <= int(cave[row][point]):
				continue
			#print([row,point],int(cave[row][point]))
			lowPoints.append([row,point])
	return lowPoints

def getRisks(cave,lowPoints):
	"""
	Sums the risk levels of each low point.
	Input: a list of n strings of m digits, and a list of points of form [x,y].
	Output: an integer.
	"""
	riskLevel = 0
	for point in lowPoints:
		riskLevel += 1 + int(cave[point[0]][point[1]])
	return riskLevel


if __name__ == "__main__":
	main()