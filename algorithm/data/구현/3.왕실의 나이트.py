N = input()
from string import ascii_lowercase

chess_map = [[0 for _ in range(9)] for _ in range(9)]

# print(chess_map)
curr_x = ascii_lowercase.index(N[0]) + 1
curr_y = int(N[1])

dx = [-1,1,-1,1,-2, -2, 2, 2]
dy = [-2,-2,2,2,-1, 1, 1, -1]

count = 0
for i in range(len(dx)):
    nx = curr_x + dx[i]
    ny = curr_y + dy[i]
    
    if nx < 1 or nx > 8 or ny < 1 or ny > 8:
        continue
    
    count += 1
    
print(count)