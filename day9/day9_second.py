def follow(hx, hy, tx, ty):
    dx, dy = hx - tx, hy - ty

    if abs(dx) < 2 and abs(dy) < 2:
        return tx, ty

    return tx + max(-1, min(dx, 1)), ty + max(-1, min(dy, 1))


with open("day9\input.txt") as f:
    visited = set()
    tails = [[0, 0] for i in range(10)]
    for line in f:
        dir, dist = line.rstrip().split()
        dist = int(dist)

        for _ in range(dist):
            if dir == 'U':
                tails[0][1] += 1
            elif dir == 'D':
                tails[0][1] -= 1
            elif dir == 'R':
                tails[0][0] += 1
            else:  # 'L'
                tails[0][0] -= 1

            for i in range(1, len(tails)):
                tails[i] = follow(*tails[i-1], *tails[i])

            visited.add(tuple(tails[-1]))

print(len(visited))
