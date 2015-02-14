image = []

with open('input.txt', 'r') as f:
    w, h = f.readline().split()
    w, h = int(w), int(h)
    for i in range(h):
        image.append(list(f.readline().strip()))
    x, y, c = f.readline().split()
    x, y = int(x), int(y)

def get_char(x, y):
    return image[(y)%h][(x)%w]

dirs = [(-1, 0), (1, 0), (0, 1), (0, -1)]

c_to_fill = get_char(x, y)

visited = set()

def fill_image(x, y, c, c_to_fill):
    if get_char(x, y) == c_to_fill:
        image[(y)%h][(x)%w] = c
        for dir_ in dirs:
            if (x+dir_[0], y+dir_[1]) in visited:
                continue
            visited.add((x+dir_[0], y+dir_[1]))
            fill_image(x+dir_[0], y+dir_[1], c, c_to_fill)

fill_image(x, y, c, c_to_fill)
print '\n'.join([''.join(row) for row in image])
