from functools import reduce
def readFile(filename) -> list[str]:
    return list(map(formatLine, open(filename).readlines()))

def formatLine(line: str) -> str:
    return line.strip()

contents = readFile('/Users/seangottschalk/advent-of-code-2022/lib/day_11.txt')

class MonkeyState:
    def __init__(self, items, operation, test, trueDest, falseDest) -> None:
        self.items = items
        self.operation = operation
        self.test = test
        self.trueDest = trueDest
        self.falseDest = falseDest

    def __str__(self):
        return f'MonkeyState(items={self.items})'
    
    def __repr__(self):
        return self.__str__()

def partA():
    monkeyMetadata = []
    for i in range(0, len(contents), 7):

        monkeyMetadata.append(MonkeyState(
            list(map(int, contents[i+1].split(": ")[1].split(", "))),
            contents[i+2].split(" = ")[1].split(" ")[1:],
            int(contents[i+3].split("divisible by ")[1]),
            int(contents[i+4].split("If true: throw to monkey ")[1]),
            int(contents[i+5].split("If false: throw to monkey ")[1]),
        ))
        print(contents[i])
    
    inspectCounts = [0] * len(monkeyMetadata)
    curRound = 1
    while curRound <= 20:
        for i in range(len(monkeyMetadata)):
            monkey = monkeyMetadata[i]
            for j in range(len(monkey.items)):
                item = monkey.items[j]
                op, amount = monkey.operation
                if op == '*':
                    if amount == 'old':
                        worry = item * item
                    else:
                        worry = item * int(amount)
                elif op == '+':
                    worry = item + int(amount)
                worry = worry // 3
                if worry % monkey.test == 0:
                    monkeyMetadata[monkey.trueDest].items.append(worry)
                else:
                    monkeyMetadata[monkey.falseDest].items.append(worry)
            inspectCounts[i] += len(monkey.items)
            monkey.items = []
        curRound += 1
    print(reduce(lambda a, b: a * b, list(reversed(sorted(inspectCounts)))[0:2]))

def partB():
    monkeyMetadata = []
    for i in range(0, len(contents), 7):

        monkeyMetadata.append(MonkeyState(
            list(map(int, contents[i+1].split(": ")[1].split(", "))),
            contents[i+2].split(" = ")[1].split(" ")[1:],
            int(contents[i+3].split("divisible by ")[1]),
            int(contents[i+4].split("If true: throw to monkey ")[1]),
            int(contents[i+5].split("If false: throw to monkey ")[1]),
        ))
    
    magicNum = reduce(lambda a, b: a * b, list(map(lambda m : m.test, monkeyMetadata)))
    
    inspectCounts = [0] * len(monkeyMetadata)
    curRound = 1
    while curRound <= 10000:
        print("working on " + str(curRound))
        for i in range(len(monkeyMetadata)):
            monkey = monkeyMetadata[i]
            for j in range(len(monkey.items)):
                item = monkey.items[j]
                op, amount = monkey.operation
                if op == '*':
                    if amount == 'old':
                        worry = item * item
                    else:
                        worry = item * int(amount)
                elif op == '+':
                    worry = item + int(amount)
                worry %= magicNum
                if worry % monkey.test == 0:
                    monkeyMetadata[monkey.trueDest].items.append(worry)
                else:
                    monkeyMetadata[monkey.falseDest].items.append(worry)
            inspectCounts[i] += len(monkey.items)
            monkey.items = []
        curRound += 1
    print(reduce(lambda a, b: a * b, list(reversed(sorted(inspectCounts)))[0:2]))

# partA()
partB()