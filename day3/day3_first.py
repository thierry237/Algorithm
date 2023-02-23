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


def findPoints(myFirstCompartiment, mySecondCompartiment):
    commonCharac = ''.join(
        set(myFirstCompartiment).intersection(mySecondCompartiment))
    return mergedDict[commonCharac]


with open('day3\input.txt') as f:
    while True:
        line = f.readline()
        if not line:
            break
        myLine = line.strip()
        compartmentLength = len(myLine)//2
        myFirstCompartiment = myLine[:compartmentLength]
        mySecondCompartiment = myLine[compartmentLength:]
        totalPoints += findPoints(myFirstCompartiment, mySecondCompartiment)

    print(totalPoints)
