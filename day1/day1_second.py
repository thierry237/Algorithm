newMaxCalories = 0
maxCalories0 = 0
maxCalories1 = 0
maxCalories2 = 0

with open('day1\input.txt') as file:
    while True:
        line = file.readline()
        if not line:
            break
        if (line == '\n'):
            if (newMaxCalories > maxCalories0):
                maxCalories2 = maxCalories1
                maxCalories1 = maxCalories0
                maxCalories0 = newMaxCalories

            elif (newMaxCalories > maxCalories1):
                maxCalories2 = maxCalories1
                maxCalories1 = newMaxCalories

            elif (newMaxCalories > maxCalories2):
                maxCalories2 = newMaxCalories

            newMaxCalories = 0
        else:
            newMaxCalories += int(line)
    print(maxCalories0 + maxCalories1 + maxCalories2)
