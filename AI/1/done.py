#!/usr/bin/python

def displayPathtoPrincess(n,grid):
   get_path()


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
    prin_coor = get_coor('p')
    # print(f'princess coordinates: {prin_coor}')
    return prin_coor

def get_path():
    path = []
    row_diff = bot_coor()[0] - princess_coor()[0]
    col_diff = bot_coor()[1] - princess_coor()[1]

    if row_diff > 0:
        # print('UP')
        rd = 'UP'
    else: 
        # print('DOWN')
        rd = 'DOWN'

    if col_diff > 0:
        # print('LEFT')
        cd = 'LEFT'
    else:
        # print('RIGHT')
        cd = 'RIGHT'

    for i in range(abs(row_diff)):
        path.append(rd)
    for i in range(abs(col_diff)):
        path.append(cd)

    ret = '\n'.join(path)
    print(ret)




m = int(input())
grid = [] 
for i in range(0, m): 
    grid.append(input().strip())

displayPathtoPrincess(m,grid)
