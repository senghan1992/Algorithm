from collections import deque

n, m = map(int, input().split())

graph = []
for i in range(n):
    graph.append(list(map(int, input())))
    

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

res = 99
def bfs(x, y, cnt):
    global res
    queue = deque([(x, y, cnt)])
    while queue:
        cx, cy, depth = queue.popleft()
        if cx == n-1 and cy == m-1:
            if res > depth:
                res = depth
        for i in range(len(dx)):
            nx, ny = cx + dx[i], cy + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m: continue
            if graph[nx][ny] == 0: continue
            queue.append((nx, ny, depth+1))
            graph[nx][ny] = 0

bfs(0,0,1)   
print(res)