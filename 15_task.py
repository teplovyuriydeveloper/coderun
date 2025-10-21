from collections import deque

def main(): 
    n = int(input())

    terra = []

    visited_points = [[[-1 for _ in range(n)] for _ in range(n)] for _ in range(n)]

    q = deque()

    for z in range(n):
        layer = []
        input()
        for y in range(n):
            row = input()
            x = row.find('S')
            if x != -1:
                q.appendleft((z, y, x))
                visited_points[z][y][x] = 0
            layer.append(row)
        terra.append(layer)

    possible_steps = [
        (-1, 0, 0), (1, 0, 0),
        (0, -1, 0), (0, 1, 0),
        (0, 0, -1), (0, 0, 1),
        ]

    while q:
        current_position = q.pop()
        count_steps = visited_points[current_position[0]][current_position[1]][current_position[2]]
        for step in possible_steps:
            new_position = (current_position[0] + step[0], current_position[1] + step[1], current_position[2] + step[2])
            if new_position[0] < 0:
                print(count_steps)
                return
            if new_position[0] < n and new_position[1] >= 0 and new_position[1] < n and new_position[2] >= 0 and new_position[2] < n:
                if terra[new_position[0]][new_position[1]][new_position[2]] == '.' and visited_points[new_position[0]][new_position[1]][new_position[2]] == -1:
                    visited_points[new_position[0]][new_position[1]][new_position[2]] = count_steps + 1
                    q.appendleft(new_position)


if __name__ == '__main__':
    main()