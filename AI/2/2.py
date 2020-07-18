
def nextMove(n, r, c, grid):
    # print(n, r, c, grid)
    print(f'n: {n}')
    print(f'r: {r}')
    print(f'c: {c}')
    print(f'grid: {grid}')

n = int(input())
r, c = [int(i) for i in input().strip().split()]
grid = []
for i in range(0, n):
    grid.append(input())

nextMove(n, r, c, grid)
