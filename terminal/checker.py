
file=open("terminal output.txt")

for line in file:
    print(line[:-1])
    print("   ",line[:line.find(" ")])
    print("   ",line[:line.find(" ")])
file.close()

