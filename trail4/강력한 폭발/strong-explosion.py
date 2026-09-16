from itertools import product
from copy import deepcopy

n = int(input())
blocks = [list(map(int, input().split())) for _ in range(n)]
original_blocks = deepcopy(blocks)
booms = sum(sum(i) for i in blocks)

bombs = product([0,1,2], repeat=booms) # 0 은 세로, 1은 십자, 2는 엑스

answer = []

bombplace = []

for i in range(n):
    for j in range(n):
        if blocks[i][j] == 1:
            bombplace.append((i,j))


def isin(i, j, n):
    return 0 <= i < n and 0 <= j < n

def vertical(blocks, i, j, n):
    if isin(i, j, n):
        blocks[i][j] = 2
    if isin(i+1, j, n):
        blocks[i+1][j] = 2
    if isin(i+2, j, n):
        blocks[i+2][j] = 2
    if isin(i-1, j, n):
        blocks[i-1][j] = 2
    if isin(i-2, j, n):
        blocks[i-2][j] = 2
    return blocks

def cross(blocks, i, j, n):
    if isin(i, j, n):
        blocks[i][j] = 2
    if isin(i+1, j, n):
        blocks[i+1][j] = 2
    if isin(i-1, j, n):
        blocks[i-1][j] = 2
    if isin(i, j+1, n):
        blocks[i][j+1] = 2
    if isin(i, j-1, n):
        blocks[i][j-1] = 2
    return blocks

def x(blocks, i, j, n):
    if isin(i, j, n):
        blocks[i][j] = 2
    if isin(i+1, j+1, n):
        blocks[i+1][j+1] = 2
    if isin(i+1, j-1, n):
        blocks[i+1][j-1] = 2
    if isin(i-1, j+1, n):
        blocks[i-1][j+1] = 2
    if isin(i-1, j-1, n):
        blocks[i-1][j-1] = 2
    return blocks

for bomb in bombs:
    for i in range(booms):
        if bomb[i] == 0:
            r, c = bombplace[i]
            blocks = vertical(blocks, r, c, n)
        elif bomb[i] == 1:
            r, c = bombplace[i]
            blocks = cross(blocks, r, c, n)
        else:
            r, c = bombplace[i]
            blocks = x(blocks, r, c, n)
    answer.append(sum(row.count(2) for row in blocks))
    blocks = deepcopy(original_blocks)

print(max(answer))