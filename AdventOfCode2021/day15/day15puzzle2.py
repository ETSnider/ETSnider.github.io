"""
Advent of Code 2021
Day 15 Challenge Part 2

Task:
The cave you are in has different risk levels in each space. You start in the top left spot, and must reach the bottom right.
You may only move horizontally and vertically, not diagonally. 
The input you are given is actually the top left tile in a 5x5 tile area, with each spot on each tile being one risk level greater than the same spots on the tiles above or to the left of it.
However, if a risk value for a spot would be greater than 9, it wraps around to 1.
Find the path with the lowest total risk, and that total risk.
"""

def getInput():
	with open("day15puzzle1input.txt",'r') as f:
		lines = f.readlines()
	outlines = []
	for line in lines:
		#print(line)
		outlines.append([int(char) for char in line.strip()])
	return outlines
	
def part2Map(caveMap):
	"""
	Expands the input map to the specifications in part 2.
	Input: n*m array of digits
	Output: 5n*5m array of digits
	"""
	xlen = len(caveMap)
	ylen = len(caveMap[0])
	outMap  = [[0 for j in range(ylen*5)] for i in range(xlen*5)]
	for i in range(xlen):
		for j in range(ylen):
			for xtile in range(5):
				for ytile in range(5):
					overflowCheck = caveMap[i][j] + xtile + ytile
					if overflowCheck > 9:
						overflowCheck -= 9
					outMap[xtile*xlen + i][ytile*ylen + j] = overflowCheck
	return outMap
	
def dijkstra(caveMap):
	"""
	Finds the weight of the least risk path from the top left to each point.
	Input: a list of lists of integers. (m*n)
	Output: a list of lists of integers. (m*n)
	"""
	riskMap=[[]]
	s = sum([sum([caveMap[i][j] for j in range(len(caveMap[0]))]) for i in range(len(caveMap))])
	for i in range(len(caveMap)):
		if i!=0:
			riskMap.append([])
		for j in range(len(caveMap[0])):
			if j==0 and i==0:
				riskMap[i].append(0)
			else:
				riskMap[i].append(s)
	unvisited = [(0,0)]
			
	for node in unvisited:
		if node[0]==len(caveMap)-1 and node[1]==len(caveMap[0])-1:
			continue;
		if node[0]==0 and node[1]==0:
			neighbours = [(node[0],node[1]+1),(node[0]+1,node[1])]
		elif node[0]==0 and node[1]==len(caveMap[0])-1:
			neighbours = [(node[0]+1,node[1]),(node[0],node[1]-1)]
		elif node[0]==len(caveMap)-1 and node[1]==0:
			neighbours = [(node[0]-1,node[1]),(node[0],node[1]+1)]
		elif node[0]==len(caveMap)-1 and node[1]==len(caveMap[0])-1:
			neighbours = [(node[0]-1,node[1]),(node[0],node[1]-1)]
		elif node[0]== 0:
			neighbours = [(node[0]+1,node[1]),(node[0],node[1]+1),(node[0],node[1]-1)]
		elif node[0]==len(caveMap)-1:
			neighbours = [(node[0]-1,node[1]),(node[0],node[1]+1),(node[0],node[1]-1)]
		elif node[1]==0:
			neighbours = [(node[0]-1,node[1]),(node[0]+1,node[1]),(node[0],node[1]+1)]
		elif node[1]==len(caveMap[0])-1:
			neighbours = [(node[0]+1,node[1]),(node[0]-1,node[1]),(node[0],node[1]-1)]
		else:
			neighbours = [(node[0]+1,node[1]),(node[0]-1,node[1]),(node[0],node[1]+1),(node[0],node[1]-1)]
		
		for neigh in neighbours:
			if riskMap[node[0]][node[1]]+caveMap[neigh[0]][neigh[1]]<riskMap[neigh[0]][neigh[1]]:
				unvisited.append(neigh)
				riskMap[neigh[0]][neigh[1]] = riskMap[node[0]][node[1]]+caveMap[neigh[0]][neigh[1]]
	return riskMap
	
def writeRiskMap(riskMap):
	"""
	Writes the final risk map to a file, for use in debugging
	"""
	with open("puzzle1out.txt","w") as f:
		for line in riskMap:
			f.write(','.join([str(x) for x in line])+'\n')

def main():
	###First, read the input from a file in the same directory, and save as a 2d array of digits.
	caveMap = getInput()
	#print(caveMap)
	###Expand the input map into the actual part 2 map.
	expCaveMap = part2Map(caveMap)
	###Next, use dijkstra's algorithm to find the least weight path.
	riskMap = dijkstra(expCaveMap)
	writeRiskMap(riskMap)
	###Output the risk of the least risk path to the console.
	print(riskMap[-1][-1])
	
if __name__ == "__main__":
	main()