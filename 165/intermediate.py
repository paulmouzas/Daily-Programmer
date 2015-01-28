with open('maze.txt', 'r') as f:
    width, height = [int(x) for x in f.readline().split()]
    maze = []
    for row in range(height):
        line = f.readline().strip()
        if 'S' in line:
            start = (row, line.index('S'))
        if 'E' in line:
            end = (row, line.index('E'))
        maze.append(list(line))
visited = [[False] * width for i in range(height)]


def find_path(maze, start, end, visited):
    if start == end:
        return True
    row, col = start
    if visited[row][col] or maze[row][col] == '#':
        return False
    visited[row][col] = True
    if maze[row - 1][col] != '#':
        if find_path(maze, (row - 1, col), end, visited):
            maze[row - 1][col] = '*'
            return True
    if maze[row + 1][col] != '#':
        if find_path(maze, (row + 1, col), end, visited):
            maze[row + 1][col] = '*'
            return True
    if maze[row][col - 1] != '#':
        if find_path(maze, (row, col - 1), end, visited):
            maze[row][col - 1] = '*'
            return True
    if maze[row][col + 1] != '#':
        if find_path(maze, (row, col + 1), end, visited):
            maze[row][col + 1] = '*'
            return True
    return False

find_path(maze, start, end, visited)
maze[end[0]][end[1]] = 'E'
print '\n'.join(''.join(row) for row in maze)
