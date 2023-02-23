with open("day5\input.txt") as f:
    slices = []
    while line := f.readline().rstrip('\r\n'):
        slices.append(line[1::4])

    stacks = [[slices[r][c] for r in range(-2, -len(slices)-1, -1)
               if slices[r][c] != ' '] for c in range(len(slices[-1]))]

    for line in f:
        num, src, dst = (int(n) for n in line.rstrip().split()[1::2])
        for i in range(int(num)):
            stacks[dst - 1].append(stacks[src - 1].pop())

    print(''.join(stack[-1] for stack in stacks))
