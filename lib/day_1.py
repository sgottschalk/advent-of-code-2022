def readFile(filename):
    return list(map(formatLine, open(filename).readlines()))

def formatLine(line):
    return line.strip()

contents = readFile('day_1_1.txt')

def partA():
    pass

def partB():
    pass