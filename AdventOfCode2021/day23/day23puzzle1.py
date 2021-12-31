"""
Advent of Code 2021
Day 23 Challenge Part 1

Task:
Amphipods come in four types: Amber, Bronze, Copper, and Dessert.
They live in a burrow that consists of a hallway and 4 side rooms. The side rooms start full, and the hall starts empty.
Diagram:
#############
#...........#
###B#C#B#D###
  #A#D#C#A#
  #########
The amphipods would like to organize such that each side room contains only 1 type of amphipod, and they are organized alphabetically from left to right.
Amphipods can move 1 space up, down, left, or right.
To move, amphipods expend energy, 1 for A, 10 for B, 100 for C, 1000 for D.
Find a way to organize the amphipods using the minimum amount of energy.

Additional rules:
    Amphipods will never stop on a space outside any room.
    Amphipods will not enter a room unless it is their destination and there are no amphipods of other types in the room.
    Once an amphipod stops in the hallway, it will not move until it can move into its room.
"""

def getInput():
    with open("day23input.txt") as f:
        lines = f.readlines()
    hallA = [lines[2][3],lines[3][3]]
    hallB = [lines[2][5],lines[3][5]]
    hallC = [lines[2][7],lines[3][7]]
    hallD = [lines[2][9],lines[3][9]]
    return hallA,hallB,hallC,hallD
    
class Node:
    def __init__(self,amph=None,roomType = None):
        self.contains = amph
        self.neighbours = []
        self.room = roomType

    def dijkstra(self,otherRoom):
        complete = []
        incomplete = [[self,0]]
        while len(incomplete)>0:
            for next in incomplete[0].neighbours:
                temp = [next[0],next[1]+incomplete[1]]
                incomplete.append(temp)
            complete.append(incomplete.pop(0))
        for node in complete:
            if node[0]==otherRoom:
                return node[1]
        raise Exception(f"Invalid room: {otherRoom}")
            
class Amphipod:
    def __init__(self,podType,spot):
        self.type = podType
        self.place = spot
        self.moved = 0
        
    def move(self,area,destination):
        distance = area.dijkstra(self.place,destination)
        self.place.contains = None
        self.place = destination
        self.place.contains = self
        self.moved += distance
    
        
class Tree:
    def __init__(hallA,hallB,hallC,hallD):
        node1 = Node()
        node2 = Node()
        node1.neighbours.append([node2,1])
        node2.neighbours.append([node1,1])
        node3 = Node()
        node2.neighbours.append([node3,2])
        node3.neighbours.append([node2,2])
        roomA1 = Node(hallA[0],'A')
        roomA2 = Node(hallA[1],'A')
        node2.neighbours.append([roomA1,2])
        roomA1.neighbours.append([node2,2])
        roomA1.neighbours.append([roomA2,1])
        roomA2.neighbours.append([roomA1,1])
        roomB1 = Node(hallB[0],'B')
        roomB2 = Node(hallB[1],'B')
        node4 = Node()
        node3.neighbours.append([roomB1,2])
        node3.neighbours.append([node4,2])
        roomB1.neighbours.append([roomB2,1])
        roomB1.neighbours.append([node4,2])
        roomB2.neighbours.append([roomB1,1])
        node4.neighbours.append([node3,2])
        node4.neighbours.append([roomB1,2])
        node5 = Node()
        node4.neighbours.apppend([node5,2])
        roomC1 = Node(hallC[0],'C')
        roomC2 = Node(hallC[1],'C')
        node4.neighbours.append([roomC1,2])
        roomC1.neighbours.append([node4,2])
        roomC1.neighbours.append([roomC2,1])
        roomC2.neighbours.append([roomC1,1])
        roomD1 = Node(hallD[0],'D')
        roomD2 = Node(hallD[1],'D')
        room6 = Node()
        room7 = Node()
        node5.neighbours.append([node4,2])
        node5.neighbours.append([node6,2])
        node5.neighbours.append([roomC1,2])
        node5.neighbours.append([roomD1,2])
        node6.neighbours.append([node5,2])
        node6.neighbours.append([roomD1,2])
        node6.neighbours.append([node7,1])
        node7.neighbours.append([node6,1])
        self.node1 = node1
        self.node2 = node2
        self.node3 = node3
        self.node4 = node4
        self.node5 = node5
        self.node6 = node6
        self.node7 = node7
        self.roomA1 = roomA1
        self.roomA2 = roomA2
        self.roomB1 = roomB1
        self.roomB2 = roomB2
        self.roomC1 = roomC1
        self.roomC2 = roomC2
        self.roomD1 = roomD1
        self.roomD2 = roomD2
        

