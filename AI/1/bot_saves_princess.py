#!/usr/bin/python
import numpy as np

def displayPathtoPrincess(n,grid):
    # ilk başta girilen değer kadarlık bir matris oluştur ve girilen değerleri direk olarak
    # matrisin içine eleman olarak gir

    # grid is a list
    """
    grid2 = []
    for line in grid:
        for char in line:
            grid2.append(char)


    # prints location of the specified array items
    arr = np.array(grid2)
    # m_ = np.where(arr == 'm')
    # m_ = np.nonzero(arr == 'm')
    arr = arr.reshape(n,n)
    m_ = np.argwhere(arr == 'm')
    p_ = np.argwhere(arr == 'p')
    print(arr)
    # print(f'coordinate of m: {m_}')
    # print(f'coordinate of p: {p_}')
    """



    """
    coor = []
    for x, y in m_:
        coor.append((x,y))

    for x, y in p_:
        coor.append((x,y))
    """


    # print(coor)
    ## coor içindeki elemanların her bir ikilisi tuple
    # print(coor[0][0])

    # karşılaştır
    # verilen n sayısına göre dynamic hale getirmek lazım
    # girilen n sayısı kadar satır ve sütun olacak

    """
    # satırlar
    # (1,1), (2,0)
    # eğer ikincinin satırı birincinin satırından büyükse down

    if coor[0][0] < coor[1][0]:
        print('down')
    elif coor[0][0] > coor[1][0]:
        print('up')

    # sütunlar
    # (1,1), (2,0)
    if coor[0][1] < coor[1][1]:
        print('right')
    elif coor[0][1] > coor[1][1]:
        print('left')
    """


    # print(len(coor))
    # this returns 2

    # satılar n tane satır var
    """
    if coor[0][0] < coor[1][0]:
        print('down')
    elif coor[0][0] > coor[1][0]:
        print('up')

    # sütunlar
    # aynı şekilde n tane sütun var
    # (1,1), (2,0)
    if coor[0][1] < coor[1][1]:
        print('right')
    elif coor[0][1] > coor[1][1]:
        print('left')
    """
    get_path()


def get_coor(val):
    for x, row in enumerate(grid):
        for y, col in enumerate(row):
            if col == val:
                return (x, y)


def bot_coor():
    bot_coord = get_coor('m')
    return bot_coord

def princess_coor():
    prin_coor = get_coor('p')
    return prin_coor

def get_path():
    row_diff = bot_coor()[0] - princess_coor()[0]
    col_diff = bot_coor()[1] - princess_coor()[1]

    if row_diff > 0:
        print('UP')
    else: 
        print('DOWN')

    if col_diff > 0:
        print('LEFT')
    else:
        print('RIGHT')







m = int(input())
grid = [] 
for i in range(0, m): 
    grid.append(input().strip())

displayPathtoPrincess(m,grid)
