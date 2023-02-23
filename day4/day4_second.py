with open("day4\input.txt") as f:
    pairs = 0
    for line in f:
        l1, r1, l2, r2 = (int(num) for a_range in line.split(',')
                          for num in a_range.split('-'))
        pairs += (l2 <= r1 and l1 <= r2)

    print(pairs)
