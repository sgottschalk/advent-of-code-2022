def readFile(filename) -> list[str]:
    return list(map(formatLine, open(filename).readlines()))

def formatLine(line: str) -> str:
    return line.strip()

contents = readFile('/Users/seangottschalk/advent-of-code-2022/lib/day_8.txt')

def parse(listOfLists: list[list[tuple[int, str]]]):
    
    visibles = []
    for i in range(len(listOfLists)):
        row = listOfLists[i]
        maxHeight = -1
        for j in range(len(row)):
            tree = row[j]
            (height, location) = tree
            if height > maxHeight:
                visibles.append(location)
                maxHeight = height
    
    for i in range(len(listOfLists)):
        row = list(reversed(listOfLists[i]))
        maxHeight = -1
        for j in range(len(row)):
            tree = row[j]
            (height, location) = tree
            if height > maxHeight:
                visibles.append(location)
                maxHeight = height
    return visibles


def partA():
    rows = [[] for i in range(len(contents))]
    cols = [[] for i in range(len(contents[0]))]
    for i in range(len(contents)):
        for j in range(len(contents[0])):
            rows[i].append((int(contents[i][j]), f'{i}_{j}'))
            cols[j].append((int(contents[i][j]), f'{i}_{j}'))

    rowCount = parse(rows)
    colCount = parse(cols)
    rowCount.extend(colCount)
    print(len(set(rowCount)))
    pass

def getScore(rNum, cNum, contents):
    num1 = 0
    rStart = rNum - 1
    cStart = cNum
    spot = int(contents[rNum][cNum])
    while rStart >= 0:
        num1 += 1
        if int(contents[rStart][cStart]) >= spot:
            break
        rStart -= 1
    if num1 == 0:
        return 0

    num2 = 0
    rStart = rNum + 1
    while rStart < len(contents):
        num2 += 1
        if int(contents[rStart][cStart]) >= spot:
            break
        rStart += 1
    if num2 == 0:
        return 0

    num3 = 0
    rStart = rNum
    cStart = cNum - 1
    while cStart >= 0:
        num3 += 1
        if int(contents[rStart][cStart]) >= spot:
            break
        cStart -= 1
    if num3 == 0:
        return 0
    
    num4 = 0
    cStart = cNum + 1
    while cStart < len(contents[0]):
        num4 += 1
        if int(contents[rStart][cStart]) >= spot:
            break
        cStart += 1
    if num4 == 0:
        return 0
    
    return num1 * num2 * num3 * num4

def partB():
    maxScore = 0
    for rNum in range(len(contents)):
        for cNum in range(len(contents)):
            curScore = getScore(rNum, cNum, contents)
            if curScore > maxScore:
                maxScore = curScore
    print(maxScore)
    pass

# partA()
partB()