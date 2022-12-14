from functools import reduce
from dataclasses import dataclass
from collections.abc import Mapping
from queue import Queue

@dataclass
class InventoryItem:
    """Class for keeping track of an item in inventory."""
    name: str
    unit_price: float
    quantity_on_hand: int = 0

    def total_cost(self) -> float:
        return self.unit_price * self.quantity_on_hand

def readFile(filename) -> list[str]:
    return list(map(formatLine, open(filename).readlines()))

def formatLine(line: str) -> str:
    return line.strip()

contents = readFile('/Users/seangottschalk/advent-of-code-2022/lib/day_12.txt')

def getKey(t):
    return f'{t[0]}_{t[1]}'

def bfs(grid, start, end):
    visited = set()
    distances = {}
    queue = Queue()
    queue.put(start)
    visited.add(getKey(start))
    while not queue.empty():
        cur = queue.get()
        curKey = getKey(cur)
        if cur == start:
            distances[curKey] = 0
        
        curRow, curCol = cur
        curHeight = grid[curRow][curCol]
        options = [[curRow - 1, curCol], [curRow + 1, curCol], [curRow, curCol - 1], [curRow, curCol + 1]]
        options = filter(lambda opt: opt[0] >= 0 and opt[0] < len(grid) and opt[1] >= 0 and opt[1] < len(grid[0]), options)
        options = list(filter(lambda opt: ord(grid[opt[0]][opt[1]]) - 1 <= ord(curHeight), options))

        for option in options:
            optKey = getKey(option)
            if optKey not in visited:
                if optKey not in distances:
                    distances[optKey] = float('inf')
                if distances[optKey] > distances[curKey] + 1:
                    distances[optKey] = distances[curKey] + 1
                if optKey == getKey(end):
                    return distances[optKey]
                queue.put(option)
                visited.add(optKey)
        

def partA():
    grid = [] * len(contents)
    start = None
    end = None
    for rowNum in range(len(contents)):
        line = contents[rowNum]
        row = []
        for colNum in range(len(line)):
            value = line[colNum]
            if value == 'S':
                start = (rowNum, colNum)
                value = 'a'
            if value == 'E':
                end = (rowNum, colNum)
                value = 'z'
            row.append(value)
        grid.append(row)

    print(bfs(grid, start, end))
    
    pass

def partB():
    grid = [] * len(contents)
    starts = []
    end = None
    for rowNum in range(len(contents)):
        line = contents[rowNum]
        row = []
        for colNum in range(len(line)):
            value = line[colNum]
            if value == 'S' or value == 'a':
                starts.append((rowNum, colNum))
                value = 'a'
            if value == 'E':
                end = (rowNum, colNum)
                value = 'z'
            row.append(value)
        grid.append(row)
    
    minDist = float('inf')
    for possibleStart in starts:
        dist = bfs(grid, possibleStart, end)
        if dist is not None and dist < minDist:
            minDist = dist
    print(minDist)
    pass

# partA()
partB()