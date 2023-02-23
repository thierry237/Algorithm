from collections import Counter

with open("day6\input.txt") as f:
    for line in f:
        count = Counter(line[:4])
        unique = len(count)

        for i in range(4, len(line.rstrip())):
            if i >= 4:
                rem = line[i - 4]
                count[rem] -= 1
                unique -= (count[rem] == 0)

            add = line[i]
            count[add] += 1
            unique += (count[add] == 1)

            if unique == 4:
                print(i + 1)
                break
