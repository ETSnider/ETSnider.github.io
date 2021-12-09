"""
Advent of Code 2021
Day 9 Challenge Part 2

Task: The lava tube you are in is filling with smoke. Only the low points of the cave are safe.
A point is s low point if it is lower than the points above, below, left and right of it.
Surrounding each low point is a basin. Basins are divided by points of height 9, which do not count as part of the basin.
Find the size of the three largesr basins, in points - including the low point - and find their product.
"""

def main():
	###First, read the cave height map from file.
	cave = getCave()
	###Next, find the low points in the cave.
	lowPoints = getLow(cave)
	###Then, find the size of each basin
	basinSizes = []
	for point in lowPoints:
		basinSizes.append(basinArea(cave,point))
	#print(basinSizes)
	###Find the 3 biggest basins.
	basinSizes.sort(reverse=True)
	basinSizes = basinSizes[:3]
	###Find the product of the areas of the 3 biggest basins, and output that product.
	#print(basinSizes)
	product = basinSizes[0] * basinSizes[1] * basinSizes[2]
	print(product)


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
	
def basinArea(cave, point):
	"""
	Find the area of a basin about a given point.
	Input: a list of strings of digits, and a list [x,y] of integers.
	Output: The number of points in the basin as an integer.
	"""
	basin = [point]
	for pt in basin:
		if pt[0]>0 and cave[pt[0]-1][pt[1]] != '9' and [pt[0]-1,pt[1]] not in basin:
			basin.append([pt[0]-1,pt[1]])
		if pt[0]<len(cave)-2 and cave[pt[0]+1][pt[1]] != '9' and [pt[0]+1,pt[1]] not in basin:
			basin.append([pt[0]+1,pt[1]])
		if pt[1]>0 and cave[pt[0]][pt[1]-1] != '9' and [pt[0],pt[1]-1] not in basin:
			basin.append([pt[0],pt[1]-1])
		if pt[1]<len(cave[0])-2 and cave[pt[0]][pt[1]+1] != '9' and [pt[0],pt[1]+1] not in basin:
			basin.append([pt[0],pt[1]+1])
	#print(len(basin))
	return len(basin)

if __name__ == "__main__":
	main()