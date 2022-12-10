def readFile(filename) -> list[str]:
    return list(map(formatLine, open(filename).readlines()))

def formatLine(line: str) -> str:
    return line.strip()

contents = readFile('/Users/seangottschalk/advent-of-code-2022/lib/day_9.txt')

def partA():
    visited = set()
    visited.add('0_0')
    hX, hY = 0, 0
    tX, tY = 0, 0
    for line in contents:
        direction, numSteps = line.split(" ")[0], int(line.split(" ")[1].strip())
        print(direction, numSteps)
        while numSteps > 0:
            if direction == 'R':
                hX += 1
            elif direction == 'L':
                hX -= 1
            elif direction == 'U':
                hY += 1
            else:
                hY -= 1
            
            if hX == tX and hY - tY == 2:
                tY += 1
            if hX == tX and tY - hY == 2:
                tY -= 1
            if hY == tY and hX - tX == 2:
                tX += 1
            if hY == tY and tX - hX == 2:
                tX -= 1
            if (hX + 2 == tX and hY - 1 == tY) or (hX + 2 == tX and hY + 1 == tY):
                tX = hX + 1
                tY = hY
            if (hX - 2 == tX and hY - 1 == tY) or (hX - 2 == tX and hY + 1 == tY):
                tX = hX - 1
                tY = hY
            if (hX - 1 == tX and hY - 2 == tY) or (hX + 1 == tX and hY - 2 == tY):
                tX = hX
                tY = hY - 1
            if (hX - 1 == tX and hY + 2 == tY) or (hX + 1 == tX and hY + 2 == tY):
                tX = hX
                tY = hY + 1
            numSteps -= 1
            visited.add(f'{tX}_{tY}')
    print(len(visited)) # 216
    pass


def partB():
    visited = set()
    visited.add('0_0')
    locations = [(0, 0) for i in range(10)]
    for line in contents:
        direction, numSteps = line.split(" ")[0], int(line.split(" ")[1].strip())
        print(direction, numSteps)
        while numSteps > 0:
            hX, hY = locations[0]
            if direction == 'R':
                hX += 1
            elif direction == 'L':
                hX -= 1
            elif direction == 'U':
                hY += 1
            else:
                hY -= 1
            locations[0] = (hX, hY)
                
            for i in range(9):
                hX, hY = locations[i]
                tX, tY = locations[i+1]
                if hX == tX and hY - tY == 2:
                    tY += 1
                if hX == tX and tY - hY == 2:
                    tY -= 1
                if hY == tY and hX - tX == 2:
                    tX += 1
                if hY == tY and tX - hX == 2:
                    tX -= 1
                if (hX + 2 == tX and hY - 1 == tY) or (hX + 2 == tX and hY + 1 == tY):
                    tX = hX + 1
                    tY = hY
                if (hX - 2 == tX and hY - 1 == tY) or (hX - 2 == tX and hY + 1 == tY):
                    tX = hX - 1
                    tY = hY
                if (hX - 1 == tX and hY - 2 == tY) or (hX + 1 == tX and hY - 2 == tY):
                    tX = hX
                    tY = hY - 1
                if (hX - 1 == tX and hY + 2 == tY) or (hX + 1 == tX and hY + 2 == tY):
                    tX = hX
                    tY = hY + 1
                if (hX + 2 == tX and hY + 2 == tY):
                    tX -= 1
                    tY -= 1
                if (hX - 2 == tX and hY - 2 == tY):
                    tX += 1
                    tY += 1
                if (hX + 2 == tX and hY - 2 == tY):
                    tX -= 1
                    tY += 1
                if (hX - 2 == tX and hY + 2 == tY):
                    tX += 1
                    tY -= 1
                locations[i] = (hX, hY)
                locations[i+1] = (tX, tY)
            print(locations)
            numSteps -= 1
            visited.add(f'{tX}_{tY}')
    print(len(visited)) # 18
    pass

# partA()
partB()