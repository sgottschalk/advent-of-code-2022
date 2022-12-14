
def readFile(filename) -> list[str]:
    return list(map(formatLine, open(filename).readlines()))

def formatLine(line: str) -> str:
    return line.strip()

contents = readFile('/Users/seangottschalk/advent-of-code-2022/lib/day_14.txt')

def makeGrid(extraX, extraY) -> list[list[int]]:
    maxX, maxY = 0, 0
    for line in contents:
        coords = line.split(" -> ")
        for coord in coords:
            x, y = list(map(lambda a: int(a), coord.split(",")))
            maxX = max(maxX, x)
            maxY = max(maxY, y)
    
    return [[None for i in range(maxY + 1 + extraY)] for j in range(maxX + 1 + extraX)] 

def fillGrid(grid: list[list[str]]) -> None:
    for line in contents:
        coords = line.split(" -> ")
        for i in range(len(coords) - 1):
            x1, y1 = list(map(lambda a: int(a), coords[i].split(",")))
            x2, y2 = list(map(lambda a: int(a), coords[i+1].split(",")))
            if x1 == x2:
                y1, y2 = sorted([y1, y2])
                for j in range(y1, y2 + 1):
                    grid[x1][j] = "#"
            else:
                x1, x2 = sorted([x1, x2])
                for j in range(x1, x2 + 1):
                    grid[j][y1] = "#"

def dropSand(grid: list[list[int]]) -> int:
    curX, curY = 500, 0
    while True:
        if curY == len(grid[0]) - 1:
            grid[curX][curY] = 'o'
            return 0
        if grid[curX][curY + 1] is None:
            curY += 1
        elif grid[curX - 1][curY + 1] is None:
            curX -= 1
            curY += 1
        elif grid[curX + 1][curY + 1] is None:
            curX += 1
            curY += 1
        else:
            if curX == 500 and curY == 0:
                return 2
            grid[curX][curY] = 'o'
            break
    return 1

def partA():
    grid = makeGrid(0, 0)
    fillGrid(grid)

    numPiecesDropped = 0
    while True:
        result = dropSand(grid)
        if result != 1:
            break
        numPiecesDropped += 1
    print(numPiecesDropped)

def partB():
    grid = makeGrid(200, 2)
    for row in grid:
        row[-1] = "#"
    fillGrid(grid)

    numPiecesDropped = 0
    while True:
        result = dropSand(grid)
        numPiecesDropped += 1
        if result == 2:
            break
    print(numPiecesDropped)

partA()
partB()