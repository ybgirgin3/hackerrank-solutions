#!/usr/bin/python

def displayPathtoPrincess():
    path = []
    row_diff = bot_coor()[0] - princess_coor()[0]
    col_diff = bot_coor()[1] - princess_coor()[1]

    # row
    if row_diff > 0:
        rd = 'UP'
    else: 
        rd = 'DOWN'

    # col
    if col_diff > 0:
        cd = 'LEFT'
    else:
        cd = 'RIGHT'

    for i in range(abs(row_diff)):
        path.append(rd)

    for i in range(abs(col_diff)):
        path.append(cd)

    ret = '\n'.join(path)
    print(ret)


def get_coor(val):
    for x, row in enumerate(grid):
        for y, col in enumerate(row):
            if col == val:
                return (x, y)

def bot_coor():
    bot_coord = get_coor('m')
    # print(f'bot coordinates: {bot_coord}')
    return bot_coord

def princess_coor():
    prin_coord = get_coor('p')
    # print(f'princess coordinates: {prin_coord}')
    return prin_coord

def is_valid(m, grid):
    if m != len(grid):
        print('matriste eksik veya fazla eleman')
    else:
        displayPathtoPrincess()


m = int(input())
grid = [] 
for i in range(0, m): 
    grid.append(input().strip())

"""
m = 3
grid = ['---', 'm--', '--p', '---']
"""

is_valid(m, grid)


