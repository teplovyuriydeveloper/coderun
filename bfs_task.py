'''
🧩 Уровень 1 — базовый BFS (решётка)
🚪 Задача 1: «Минимальное количество шагов до выхода из лабиринта»

Условие:
Дана прямоугольная карта размера N × M, состоящая из:

'.' — свободная клетка,

'#' — стена,

'S' — старт,

'E' — выход.

Найди минимальное количество шагов, чтобы дойти от S до E.
Ходить можно только по четырём направлениям (вверх, вниз, влево, вправо).

Ввод пример:

5 6
######
#S...#
#.##.#
#....#
##E###


Вывод:

7
'''

from collections import deque

def main():

    sy, sx = map(int, input().split())

    map_matrix = []

    start_x = -1
    start_y = -1

    for i in range(sy):
        floor = input()
        if floor.find('S') != -1:
            start_y = i
            start_x = floor.find('S')

        map_matrix.append(floor)

    dn = [[-1] * sx for i in range(sy)]

    q = deque()

    q.appendleft((start_y, start_x))

    dn[start_y][start_x] = 0

    available_steps = ((1, 0), (1, 0), (0, -1), (0, 1))

    while q:
        item = q.pop()

        for s in available_steps:
            if dn[item[0] + s[0]][item[1] + s[1]] == -1 and map_matrix[item[0] + s[0]][item[1] + s[1]] == '.':
                dn[item[0] + s[0]][item[1] + s[1]] = dn[item[0]][item[1]] + 1
                q.appendleft((item[0] + s[0], item[1] + s[1]))
            elif dn[item[0] + s[0]][item[1] + s[1]] == -1 and map_matrix[item[0] + s[0]][item[1] + s[1]] == 'E':
                dn[item[0] + s[0]][item[1] + s[1]] = dn[item[0]][item[1]] + 1
                print(dn[item[0] + s[0]][item[1] + s[1]])
                break



    



    
    


if __name__ == '__main__':
    main()