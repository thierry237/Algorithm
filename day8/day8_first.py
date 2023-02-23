with open("day8\input.txt") as f:
    forest = [line.rstrip() for line in f.readlines()]

width = len(forest[0])
height = len(forest)
unseen = [[True] * width for _ in range(height)]


def in_bounds(x, y):
    return 0 <= x < width and 0 <= y < height


count = 0
x = y = 0
dx, dy = 0, 1
ndx, ndy = 1, 0

while True:
    r_max = '\0'
    rx, ry = x, y
    while in_bounds(rx, ry) and r_max != '9':
        t_height = forest[ry][rx]
        if t_height > r_max:
            count += unseen[ry][rx]
            unseen[ry][rx] = False
            r_max = t_height

        rx, ry = rx + ndx, ry + ndy

    nx, ny = x + dx, y + dy
    if in_bounds(nx, ny):
        x, y = nx, ny
    else:
        dx, dy = ndx, ndy
        ndx, ndy = ndy, -ndx

    if (x, y) == (0, 0) and (dx, dy) == (0, 1):
        break

print(count)
