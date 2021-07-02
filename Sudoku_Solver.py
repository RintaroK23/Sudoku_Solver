import numpy as np

grid = []
n = 1

def check(y, x):
    global grid
    check_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    gy = (y // 3) * 3
    gx = (x // 3) * 3
    # 3x3単位で調べる
    for i in range(0, 3):
        for j in range(0, 3):
            if grid[gy + i][gx + j] in check_list:
                check_list.remove(grid[gy + i][gx + j])
    
    # 行単位で調べる
    for cx in range(0, 9):
            if grid[y][cx] in check_list:
                check_list.remove(grid[y][cx])
    # 列単位で調べる
    for ry in range(0, 9):
            if grid[ry][x] in check_list:
                check_list.remove(grid[ry][x])

    return check_list

def solver():
    global grid, n
    for y in range(0, 9):
        for x in range(0, 9):
            if grid[y][x] == 0:
                for i in check(y, x):
                    grid[y][x] = i
                    solver()
                    grid[y][x] = 0
                return
    print('---------------------')
    print('解答', n)
    n += 1
    print(np.matrix(grid))

def make_grid():
    global grid
    print('問題をスペース、カンマなどを入れずに1行ずつ入力(空欄は0を入力)')
    for i in range(9):
        a = input()
        lis = list(map(int, a))
        grid.append(lis)
    print('入力した問題')
    print(np.matrix(grid))

make_grid()
solver()