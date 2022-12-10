def readFile(filename) -> list[str]:
    return list(map(formatLine, open(filename).readlines()))

def formatLine(line: str) -> str:
    return line.strip()

contents = readFile('/Users/seangottschalk/advent-of-code-2022/lib/day_10.txt')

def partA():
    curVal = 1
    curCycle = 1
    totalVal = 0
    interestingIndices = set([20, 60, 100, 140, 180, 220])
    for line in contents:
        if line == 'noop':
            pass
        else:
            curCycle += 1
            if curCycle in interestingIndices:
                totalVal += curCycle * curVal
            _, num = line.split(" ")
            curVal += int(num)
        curCycle += 1
        if curCycle in interestingIndices:
            totalVal += curCycle * curVal
    
    print(totalVal)

def updateResult(result, curCycle, curVal):
    spritePosition = [curVal + i for i in range(-1, 2)]
    pixelVal = "#" if ((curCycle - 1) % 40) in spritePosition else '.'
    row = (curCycle - 1) // 40
    result[row].append(pixelVal)

def partB():
    curVal = 1
    curCycle = 1
    result = [[] for _ in range(6)]
    for line in contents:
        if line == 'noop':
            updateResult(result, curCycle, curVal)
            curCycle += 1
        else:
            updateResult(result, curCycle, curVal)
            curCycle += 1
            updateResult(result, curCycle, curVal)
            _, num = line.split(" ")
            curVal += int(num)
            curCycle += 1
    
    for list in result:
        print("".join(list))

partA()
partB()