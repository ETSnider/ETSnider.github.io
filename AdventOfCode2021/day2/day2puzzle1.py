import io
"""
Advent of Code 2021
Day 2 Challenge Part 1

Task:
Given a series of commands to a submarine, calculate its position and depth, and calculate the depth times the horizontal position.
Commands: 
"up X" - subtract X from depth
"down X" - add X to depth
"forward X" - add X to horizontal position
"""
def main():
	###First, read the list of commands from a file in the same directory.
	horizontal=0
	depth=0
	f=open("day2puzzle1input.txt",'r')
	cmds=f.readlines()
	f.close()
	###Then translate and implement each command as specified/
	for cmd in cmds:
		cmd=cmd.split()
		if cmd[0]=="forward":
			horizontal=horizontal+int(cmd[1])
		elif cmd[0]=="down":
			depth=depth+int(cmd[1])
		else:
			depth=depth-int(cmd[1])
	###Finally, multiply the final depth and horizontal position, and output the result to the console.
	print(horizontal*depth)

if __name__=="__main__":
	main()