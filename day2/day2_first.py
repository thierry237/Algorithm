resultWin = 0
resultOption = 0


def winner(opponentInput, myInput):

    global resultWin
    global resultOption

    match opponentInput:
        case 'A':
            match myInput:
                case 'X':
                    resultWin += 3
                    resultOption += 1
                case 'Y':
                    resultWin += 6
                    resultOption += 2
                case 'Z':
                    resultWin += 0
                    resultOption += 3
                case _:
                    print('impossible')
        case 'B':
            match myInput:
                case 'X':
                    resultWin += 0
                    resultOption += 1
                case 'Y':
                    resultWin += 3
                    resultOption += 2
                case 'Z':
                    resultWin += 6
                    resultOption += 3
                case _:
                    print('impossible')
        case 'C':
            match myInput:
                case 'X':
                    resultWin += 6
                    resultOption += 1
                case 'Y':
                    resultWin += 0
                    resultOption += 2
                case 'Z':
                    resultWin += 3
                    resultOption += 3
                case _:
                    print('impossible')
        case _:
            print('impossible')


with open('day2\input.txt') as file:
    while True:
        line = file.readline()
        if not line:
            break
        inputsArray = line.split()
        winner(inputsArray[0], inputsArray[1])
print(resultWin + resultOption)
