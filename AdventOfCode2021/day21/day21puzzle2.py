"""
Advent of Code 2021
Day 21 Challenge Part 2

Task:
You are challenged to a game of Dirac Dice. This consists of a single die, two pawns, and a game board with a circular track and spaces marked 1 through 10 clockwise.
You start on a random space given by your puzzle input. Player 1 goes first.

Players take turns moving. Each player rolls the die 3 times, sums the numbers, and moves that many spaces forward around the track.
Each space you stop on, the space number is added to your score. The game ends when any player's score reaches 21.
This game uses a dirac die: when rolled, it splits the universe into 3, with the first univers rolling a 1, the second rolling a 2, and the third rolling a 3.
Find all possible outcomes. Which player wins in more universes, and how many universes does the player win in?

This approach used too much memory, refactored in day21puzzle2v2.py
"""

def getInput():
    with open("day21input.txt",'r') as f:
        lines = f.readlines()
    out = []
    for line in lines:
        out.append(int(line.strip().split()[-1]))
    return out
    
class Universe:
    def __init__(self,p1Pos,p2Pos,turnNum = 0,p1Score = 0,p2Score = 0,roll = None):
        self.turn = turnNum
        self.player1 = p1Score
        self.player2 = p2Score
        self.p1Position = p1Pos
        self.p2Position = p2Pos
        if roll!=None:
            self.advance(roll)
    
    def player1Score(self,roll):
        self.p1Position += roll
        if self.p1Position >10:
            self.p1Position -= 10
        self.player1 += self.p1Position
        self.turn = 1
        
    def player2Score(self,roll):
        self.p2Position += roll
        if self.p2Position>10:
            self.p2Position -= 10
        self.player2 += self.p2Position
        self.turn = 0

    def advance(self,roll):
        if self.turn == 0:
            self.player1Score(roll)
        elif self.turn == 1:
            self.player2Score(roll)
        else:
            raise Exception(f"improper turn {self.turn}")
    
    def getPlayer1(self):
        return self.player1
        
    def getPlayer2(self):
        return self.player2

    def __repr__(self):
        return f"Turn: {self.turn}, P1 Score = {self.player1}, P2 Score = {self.player2}, P1 Position = {self.p1Position}, P2 Position = {self.p2Position}"

def roll(universe):
    for i in range(1,4):
        for j in range(1,4):
            for k in range(1,4):
                yield Universe(universe.p1Position,universe.p2Position,universe.turn,universe.player1,universe.player2,i+j+k)
    
def main():
    ###First, read the starting positions of the characters from a file.
    startPositions = getInput()
    #startPositions = [4,8]
    ###Use these to create the initial universe, within a list
    multiverse = [Universe(p1Pos = startPositions[0],p2Pos = startPositions[1])]
    ###Also start a count of the universes in which each player won
    p1Wins = 0
    p2Wins = 0
    ###For each universe in the multiverse, roll, and add the resulting universes to the multiverse unless they are complete.
    while(len(multiverse)>0):
        #print(multiverse[0])
        for variant in roll(multiverse[0]):
            if variant.getPlayer1()>=21:
                p1Wins += 1
            elif variant.getPlayer2()>=21:
                p2Wins += 1
            else:
                multiverse.append(variant)
        multiverse.pop(0)
    ###After iterating through all the possible universes, output the number of universees each player won to the console
    print(p1Wins,p2Wins)
    

if __name__ == "__main__":
    main()