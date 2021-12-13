"""
Advent of Code 2021
Day 12 Challenge Part 2

Task: A cave system consists of a series of caves and connecting tunnels.
The caves may be big or small. One small cave may be passed through twice, and all others must be passed through once.
You may not return to the "start" cave.
You begin at the "start" cave, and finish at the "end" cave.
Given a list of the paths between caves, find the number of unique paths between the start and end caves.
"""
import networkx as nx

def main():
	###First, read the connections from input file in the same directory.
	connections = getConnections()
	#print(connections)
	###Next, create and populate the graph.
	caveSystem = nx.Graph()
	for branch in connections:
		caveSystem.add_edge(branch[0],branch[1])
	#print(list(caveSystem.nodes))
	#print(list(caveSystem.neighbors('start')))
	###Then, count the paths from start to end, and output it to the console.
	count = sum(1 for x in getPaths(caveSystem,['start'],True) if x[-1]=='end')
	print(count)

	
	

def getConnections():
	with open("day12puzzle1input.txt",'r') as f:
		input = f.readlines()
	connections = []
	for connection in input:
		left, right = connection.strip().split('-')[0].split(','),connection.strip().split('-')[1]
		for cave in left:
			connections.append([cave,right])
	return connections
	
def getPaths(caveSystem, path, double_visit):
	current = path[-1]
	#print(path)
	#print(list(caveSystem.neighbors('start')))
	for cave in list(caveSystem.neighbors(current)):
		if cave == 'end':
			yield path+[cave]
		elif cave.lower()==cave and cave in path:
			if double_visit and cave != 'start':
				yield from getPaths(caveSystem,path + [cave],False)
			else:
				continue
		else:
		   	yield from getPaths(caveSystem,path + [cave],double_visit)
	
	
	
if __name__ == "__main__":
	main()