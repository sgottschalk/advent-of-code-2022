def readFile(filename) -> list[str]:
    return list(map(formatLine, open(filename).readlines()))

def formatLine(line):
    return line.strip()

contents = readFile('/Users/seangottschalk/advent-of-code-2022/lib/day_3.txt')

def partA():
    total = 0
    for line in contents:
        print(line)
        firstHalf = set(line[:len(line)//2-1])
        secondHalf = set(line[len(line)//2:])
        letter = firstHalf.intersection(secondHalf).pop()
        if letter.islower():
            total += ord(letter) - ord('a') + 1
        else:
            total += ord(letter) - ord('A') + 27
    return total

print(partA())

def partB():
    pass
