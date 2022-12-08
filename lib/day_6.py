def readFile(filename) -> list[str]:
    return list(map(formatLine, open(filename).readlines()))

def formatLine(line: str) -> str:
    return line

contents = readFile('/Users/seangottschalk/advent-of-code-2022/lib/day_6.txt')

def partA():
    for line in contents:
        chars = [None] * 4
        for i in range(len(line)):
            chars[i % 4] = line[i]
            if i >= 3:
                charsSet = set(chars)
                if len(charsSet) == 4:
                    print(i+1)
                    break
    pass

def partB():
    for line in contents:
        chars = [None] * 14
        for i in range(len(line)):
            chars[i % 14] = line[i]
            if i >= 13:
                charsSet = set(chars)
                if len(charsSet) == 14:
                    print(i+1)
                    break
    pass

partA()
partB()