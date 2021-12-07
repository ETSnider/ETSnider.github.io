import io
"""
Advent of Code 2021
Day 3 Challenge Part 1

Task: 
Given a series of binary numbers from a life support diagnostic report, calculate the O2 scrubber rating and CO2 scrubber rating by following the selection criteria.
O2 criteria: For each bit position, find the most common value, and keep only the numbers with that value in that position.
	If there is a tie, keep values with a 1 in that position.
CO2 criteria:For each bit position, find the least common value, and keep only the numbers with that value in that poosition.
	If there is a tie, keep values with a 0 in that position.
Multiply the O2 rating and the CO2 rating to find the life support rating.
"""

def main():
	###First, read the numbers from a file in the same directory.
	f=open("day3puzzle1input.txt",'r')
	diagnostics = f.readlines()
	f.close()
	###Then, duplicate the values into two lists, one for each rating to find.
	diagO2 = []
	diagCO2 = []
	for line in diagnostics:
		diagO2.append(line)
		diagCO2.append(line)
	###Next, seive through the first list by the O2 criteria to find the O2 rating.
	count0 = 0
	count1 = 0
	bit = 0
	while len(diagO2)>1 and bit<=12:
		for i in range(len(diagO2)):
			if diagO2[i][bit]=="0":
				count0 += 1
			else:
				count1 += 1
		if count0 > count1:
			diagO2 = list(line for line in diagO2 if line[bit]=="0")
		else:
			diagO2 = list(line for line in diagO2 if line[bit]=="1")
		bit += 1
		count0 = 0
		count1 = 0
	###Seive through the second list by the CO2 criteria to find the CO2 rating.
	bit = 0
	while len(diagCO2)>1 and bit<=12:
		for i in range(len(diagCO2)):
			if diagCO2[i][bit]=="0":
				count0 += 1
			else:
				count1 += 1
		if count0 <= count1:
			diagCO2 = list(line for line in diagCO2 if line[bit]=="0")
		else:
			diagCO2 = list(line for line in diagCO2 if line[bit]=="1")
		bit += 1
		count0 = 0
		count1 = 0	
	###Convert the O2 rating and CO2 rating to integers.
	oxyGen = int(diagO2[0],2)
	CO2Scrub = int(diagCO2[0],2)
	print(bin(oxyGen))
	print(bin(CO2Scrub))
	###Multiply the O2 rating and CO2 rating to find the life support rating, and output it to the console.
	print(oxyGen * CO2Scrub)
	

if __name__=="__main__":
	main()