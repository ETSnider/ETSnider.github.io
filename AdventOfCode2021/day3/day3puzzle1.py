import io
"""
Advent of Code 2021
Day 3 Challenge Part 1

Task: 
Given a series of binary numbers from a generator diagnostic report, calculate the gamma by finding the most common value of each bit,and calculate the epsilon by finding the least common value of each bit.
Multiply the gamma and the epsilon to get the power consumption.
"""

def main():
	###First, get the numbers from a file in the same directory.
	f=open("day3puzzle1input.txt",'r')
	diagnostics = f.readlines()
	f.close()
	###Next, count the number of 0s and 1s in each position.
	diaglen = 12
	count = []
	mostcommon = []
	for i in range(diaglen):
		count.append([0,0])
		mostcommon.append(0)
		
	for line in diagnostics:
		for i in range(diaglen):
			if line[i]=="1":
				count[i][1] = count[i][1] + 1
			else:
				count[i][0] = count[i][0] + 1
	###Determine whether there were more 0s or 1s for each bit, and use that to calculate the gamma.
	for i in range(len(count)):
		if count[i][0]>count[i][1]:
			mostcommon[i]="0"
		else:
			mostcommon[i]="1"

	gamma = int("".join(str(x) for x in mostcommon),2)
	###Calculate the epsilon by XORing the gamma with a mask of all 1s.
	epsilon = 0xFFF ^ gamma
	#print(bin(gamma))
	#print(bin(epsilon))
	###Multiply the gamma and epsilon to find the power consumption, and output it to the console.
	print(gamma*epsilon)

if __name__=="__main__":
	main()