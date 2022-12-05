import re

def readFile(filename) -> list[str]:
    return list(map(formatLine, open(filename).readlines()))

def formatLine(line):
    return line

contents = readFile('/Users/seangottschalk/advent-of-code-2022/lib/day_5.txt')

def partA():
    stacks = [[] for i in range(1, len(contents[0]), 4)]
    print(stacks)
    for line in contents:
        if line.startswith(" 1"):
            break
        else:
            stackNum = 0
            for i in range(1, len(line), 4):
                stacks[stackNum].append(line[i])
                stackNum += 1
    stacks = [stack[::-1] for stack in stacks]
    stacks = [[elem for elem in stack if elem is not ' '] for stack in stacks]
    print(stacks)

    for line in contents:
        if line.startswith("move "):
            numMoved, movedFrom, movedTo = list(map(int, [elem.strip() for elem in re.split('move | from | to ', line) if elem]))
            movedFrom -= 1
            movedTo -= 1
            while numMoved > 0:
                toMove = stacks[movedFrom].pop(-1)
                stacks[movedTo].append(toMove)
                numMoved -= 1
    final = ''
    for stack in stacks:
        final += stack[-1]
    print(final)
    pass

def partB():
    stacks = [[] for i in range(1, len(contents[0]), 4)]
    print(stacks)
    for line in contents:
        if line.startswith(" 1"):
            break
        else:
            stackNum = 0
            for i in range(1, len(line), 4):
                stacks[stackNum].append(line[i])
                stackNum += 1
    stacks = [stack[::-1] for stack in stacks]
    stacks = [[elem for elem in stack if elem is not ' '] for stack in stacks]
    print(stacks)

    for line in contents:
        if line.startswith("move "):
            numMoved, movedFrom, movedTo = list(map(int, [elem.strip() for elem in re.split('move | from | to ', line) if elem]))
            movedFrom -= 1
            movedTo -= 1
            toMove = []
            while numMoved > 0:
                toMove.append(stacks[movedFrom].pop(-1))
                numMoved -= 1
            toMove.reverse()
            stacks[movedTo].extend(toMove)
    final = ''
    for stack in stacks:
        final += stack[-1]
    print(final)
    pass

partA()
partB()