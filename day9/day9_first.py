with open("day9\input.txt") as f:
    visited = set()
    hx = hy = tx = ty = 0
    for line in f:
        dir, dist = line.rstrip().split()
        dist = int(dist)

        for _ in range(dist):
            ohx, ohy = hx, hy
            if dir == 'U':
                hy += 1
            elif dir == 'D':
                hy -= 1
            elif dir == 'R':
                hx += 1
            else:  # 'L'
                hx -= 1

            if abs(hx - tx) > 1 or abs(hy - ty) > 1:
                tx, ty = ohx, ohy

            visited.add((tx, ty))

print(len(visited))
