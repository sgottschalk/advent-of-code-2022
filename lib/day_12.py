from functools import reduce
from dataclasses import dataclass
from collections.abc import Mapping

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

def findEnd(grid: list[list[str]], cur: tuple[int, int], end: tuple[int, int], visited: set[str], memo: Mapping[str, int]) -> int:
    memoLookupKey = f'{cur[0]}_{cur[1]}'
    if memoLookupKey in memo:
        return memo[memoLookupKey]
    
    if cur[0] == end[0] and cur[1] == end[1]:
        memo[memoLookupKey] = 0
        return 0
    
    visited.add(memoLookupKey)
    
    curRow, curCol = cur
    curHeight = grid[curRow][curCol]
    options = [[curRow - 1, curCol], [curRow + 1, curCol], [curRow, curCol - 1], [curRow, curCol + 1]]
    options = filter(lambda opt: opt[0] >= 0 and opt[0] < len(grid) and opt[1] >= 0 and opt[1] < len(grid[0]), options)
    options = filter(lambda opt: f'{opt[0]}_{opt[1]}' not in visited, options)
    options = list(filter(lambda opt: abs(ord(curHeight) - ord(grid[opt[0]][opt[1]])) <= 1, options))
    if len(options) == 0:
        memo[memoLookupKey] = float('inf')
        return float('inf')
    
    minFound = float('inf')
    for option in options:
        minForOption = findEnd(grid, option, end, visited, memo)
        if minForOption < minFound:
            minFound = 1 + minForOption
    
    memo[memoLookupKey] = minFound
    visited.remove(memoLookupKey)
    return minFound


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

    visited: set[str] = set()
    memo: Mapping[str, int] = {}
    print(findEnd(grid, start, end, visited, memo))
    
    pass

def partB():
    pass

partA()
partB()