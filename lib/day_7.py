def readFile(filename) -> list[str]:
    return list(map(formatLine, open(filename).readlines()))

def formatLine(line: str) -> str:
    return line

contents = readFile('/Users/seangottschalk/advent-of-code-2022/lib/day_7.txt')

class Entry:
    def __init__(self, typeOrSize, name, parent):
        self.typeOrSize = typeOrSize
        self.name = name
        self.parent = parent
        self.children = []
    
    def getChild(self, typeOrSize, name):
        for i in range(len(self.children)):
            if self.children[i].name == name:
                return self.children[i]
        child = Entry(typeOrSize, name, self)
        self.children.append(child)
        return child
    
    def setSize(self, size):
        self.size = size
    
    def __str__(self):
        return f'Entry(t={self.typeOrSize}, n={self.name}, p={self.parent}, c={self.children})'
    
    def __repr__(self):
        return self.__str__()

def getDirs(curEntry: Entry, matchedDirSizes: list[int], targetSize: int):
    if curEntry.typeOrSize != 'dir':
        return int(curEntry.typeOrSize)
    
    childSizes = list(map(lambda x: getDirs(x, matchedDirSizes, targetSize), curEntry.children))
    childSizesSum = sum(childSizes)
    curEntry.setSize(childSizesSum)
    if childSizesSum > targetSize:
        matchedDirSizes.append(childSizesSum)
    
    return childSizesSum

def partA():
    rootEntry = Entry('dir', '/', None)
    curEntry = rootEntry
    for line in contents:
        print("===")
        print(line)
        if line.startswith("$ cd"):
            dest = line[5:].strip()
            if dest == '..':
                curEntry = curEntry.parent
            elif dest == '/':
                pass
            else:
                curEntry = curEntry.getChild('dir', dest)
        elif line.startswith("$ ls"):
            pass
        else:
            typeOrSize, entityName = list(map(lambda x: x.strip(), line.split(" ")))
            print('a', typeOrSize, entityName)
            curEntry.getChild(typeOrSize, entityName)
    
    matchedDirSizes = []
    getDirs(rootEntry, matchedDirSizes, 0)
    curUnusedSize = 70000000 - rootEntry.size
    targetSize = 30000000 - curUnusedSize
    matchedDirSizes = []
    getDirs(rootEntry, matchedDirSizes, targetSize)
    print(min(matchedDirSizes))

def partB():
    pass

partA()
partB()