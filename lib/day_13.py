import ast
from functools import cmp_to_key

def readFile(filename) -> list[str]:
    return list(map(formatLine, open(filename).readlines()))

def formatLine(line: str) -> str:
    return line.strip()

contents = readFile('/Users/seangottschalk/advent-of-code-2022/lib/day_13.txt')

def isInRightOrder(firstLine, secondLine):
    if isinstance(firstLine, str):
        firstPacket = ast.literal_eval(firstLine)
        secondPacket = ast.literal_eval(secondLine)
    else:
        firstPacket = firstLine
        secondPacket = secondLine
    for j in range(min(len(firstPacket), len(secondPacket))):
        firstElem = firstPacket[j]
        secondElem = secondPacket[j]
        if isinstance(firstElem, int) and isinstance(secondElem, int):
            if firstElem == secondElem:
                continue
            elif firstElem < secondElem:
                return True
            else:
                return False
        elif isinstance(firstElem, list) and isinstance(secondElem, list):
            res = isInRightOrder(firstElem, secondElem)
            if res != None:
                return res
        else:
            if isinstance(firstElem, int):
                firstElem = [firstElem]
            else:
                secondElem = [secondElem]
            res = isInRightOrder(firstElem, secondElem)
            if res != None:
                return res
    if len(firstPacket) == len(secondPacket):
        return None
    return len(firstPacket) < len(secondPacket)

def partA():
    sum = 0
    for i in range(0, len(contents), 3):
        res = isInRightOrder(contents[i], contents[i+1])
        if res:
            sum += ((i // 3) + 1)
    print(sum)

def partBHelper(a, b):
    res = isInRightOrder(a, b)
    if res:
        return -1
    else:
        return 1

def partB():
    inputLines = [l for l in contents if l != ''] + ["[[2]]", "[[6]]"]
    packetsSorted = sorted(inputLines, key=cmp_to_key(partBHelper))
    product = 1
    for i in range(len(packetsSorted)):
        packet = packetsSorted[i]
        if packet in ["[[2]]", "[[6]]"]:
            product *= (i + 1)
    print(product)

# partA()
partB()