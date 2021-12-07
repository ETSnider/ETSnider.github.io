"""
Advent of Code 2021
Day 1 Challenge Part 1

Task: read a series of number from a file, and count the number of times a number is greater than the previous number.
"""
import sys

#import requests
#from bs4 import BeautifulSoup

def getList():
	"""
	Read a list of numbers from a file in the same directory.
	Output: A list of integers.
	"""
	f = open('day1puzzle1input.txt','r')
	nums = f.read()
	f.close()
	nums = nums.split()
	for n in range(len(nums)):
		nums[n]=int(nums[n])
	return nums
	
def countDrops(numlist):
	"""
	Count the number of times a number in a list is greater than the previous number.
	Input: A list of integers.
	Output: An integer.
	"""
	count=0
	for num in range(1,len(numlist)):
		if numlist[num]-numlist[num-1]>0:
			count=count+1
	return count
	
def main():
	#testnums=[199,200,208,210,200,207,240,269,260,263]
	#print(countDrops(testnums))
	###First, read the numbers from a file in the same directory as a list of integers.
	numlist = getList()
	###Next, count the number of times a number is greater than the preceding number, and print this count to the console.
	count = countDrops(numlist)
	print(str(count))
	return 1

if __name__=="__main__":
	main()
