with open("day8\input.txt") as f:
    forest = [line.rstrip() for line in f.readlines()]

width = len(forest[0])
height = len(forest)
scores = [[1] * width for _ in range(height)]


def in_bounds(x, y):
    return 0 <= x < width and 0 <= y < height


max_score = 0
x = y = 0
dx, dy = 0, 1
ndx, ndy = 1, 0

while True:
    m_stack = [('\0', -1)]
    rx, ry, rl = x, y, 0
    while in_bounds(rx, ry):
        t_height = forest[ry][rx]

        while m_stack and t_height > m_stack[-1][0]:
            m_stack.pop()

        if not m_stack:
            r_view = rl
        elif t_height == m_stack[-1][0]:
            r_view = rl - m_stack[-1][1]
            m_stack.pop()
        else:
            r_view = rl - m_stack[-1][1]

        m_stack.append((t_height, rl))

        scores[ry][rx] *= r_view
        if ry * rx * rl > 0 and scores[ry][rx] > max_score:
            max_score = scores[ry][rx]

        rx, ry, rl = rx + ndx, ry + ndy, rl + 1

    nx, ny = x + dx, y + dy
    if in_bounds(nx, ny):
        x, y = nx, ny
    else:
        dx, dy = ndx, ndy
        ndx, ndy = ndy, -ndx

    if (x, y) == (0, 0) and (dx, dy) == (0, 1):
        break

print(scores)
print(max_score)
