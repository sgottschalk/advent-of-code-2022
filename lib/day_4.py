def readFile(filename) -> list[str]:
    return list(map(formatLine, open(filename).readlines()))

def formatLine(line):
    return line.strip()

contents = readFile('/Users/seangottschalk/advent-of-code-2022/lib/day_4.txt')

def partA():
    sum = 0
    for line in contents:
        parts = line.split(",")
        elfA = parts[0]
        elfB = parts[1]
        elfAParts = elfA.split("-")
        elfBParts = elfB.split("-")
        if int(elfAParts[0]) >= int(elfBParts[0]) and int(elfAParts[1]) <= int(elfBParts[1]):
            sum += 1
        if int(elfBParts[0]) >= int(elfAParts[0]) and int(elfBParts[1]) <= int(elfAParts[1]):
            sum += 1
        if elfA == elfB:
            sum -= 1
    print(sum)

def partB():
    sum = 0
    for line in contents:
        parts = line.split(",")
        elfA = parts[0]
        elfB = parts[1]
        elfAParts = list(map(int, elfA.split("-")))
        elfBParts = list(map(int, elfB.split("-")))
        
        if elfAParts[0] <= elfBParts[0] and elfBParts[0] <= elfAParts[1]:
            sum += 1
        elif elfBParts[0] <= elfAParts[1] and elfAParts[0] <= elfBParts[1]:
            sum += 1
    print(sum)

partB()