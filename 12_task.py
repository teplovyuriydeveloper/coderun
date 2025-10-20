from collections import deque

def bfs(dn, start_x, start_y):
    N, M = len(dn), len(dn[0])
    q = deque()
    q.append((start_x, start_y))
    dn[start_x][start_y] = 0

    moves = [
        (-1, -2), (-2, -1),
        (1, -2),  (2, -1),
        (-1, 2),  (-2, 1),
        (1, 2),   (2, 1)
    ]

    while q:
        x, y = q.popleft()
        for dx, dy in moves:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < M:
                if dn[nx][ny] == -1:
                    dn[nx][ny] = dn[x][y] + 1
                    q.append((nx, ny))



def main():

    N, M, S, T, Q = map(int, input().split())

    dn = [[-1] * M for i in range(N)]

    dn[S-1][T-1] = 0

    all_actors = []

    for _ in range(Q):
        x, y = map(int, input().split())

        all_actors.append((x-1, y-1))

    bfs(dn, S-1, T-1)

    total = 0

    for actor in all_actors:
        if dn[actor[0]][actor[1]] == -1:
            total = -1
            break
        else: 
            total += dn[actor[0]][actor[1]]

    print(total)



if __name__ == '__main__':
    main()
