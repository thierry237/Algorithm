import string
alphabetLowArray = list(string.ascii_lowercase)
alphabetUpArray = list(string.ascii_uppercase)

priorityLowList = list(range(1, 27))
priorityHighList = list(range(27, 53))

dictLow = dict(zip(alphabetLowArray, priorityLowList))
dictHigh = dict(zip(alphabetUpArray, priorityHighList))

mergedDict = {**dictLow, **dictHigh}

totalPoints = 0
groups = []


def findPointsSecond(myFirstLine, mySecondLine, myThirdLine):
    commonCharac = ''.join(set(myFirstLine).intersection(
        set(mySecondLine)).intersection(set(myThirdLine)))
    return mergedDict[commonCharac]


with open('day3\input.txt') as f:
    while True:
        line = f.readline()
        if not line:
            break
        myLine = line.strip()
        groups.append(myLine)
        if (len(groups) == 3):
            totalPoints += findPointsSecond(groups[0], groups[1], groups[2])
            groups = []

    print(totalPoints)
