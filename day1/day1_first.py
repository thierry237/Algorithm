newMaxCalories = 0
maxCalories = 0


with open('day1\input.txt') as file:
    while True:
        line = file.readline()
        if not line:
            break
        if (line != '\n'):
            newMaxCalories += int(line)
            if (newMaxCalories > maxCalories):
                maxCalories = newMaxCalories
        else:
            newMaxCalories = 0

print(maxCalories)
