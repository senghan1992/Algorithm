n, m = map(int, input().split())

graph = []

for i in range(n):
    graph.append(list(map(int, input())))

res = 99
def dfs(x, y, cnt):
    global res
    if x < 0 or x >= n or y < 0 or y >= m:
        return False
    if x == n-1 and y == m-1:
        if res > cnt:
            res = cnt
    if graph[x][y] == 1:
        graph[x][y] = 0
        dfs(x+1, y, cnt+1)
        dfs(x-1, y, cnt+1)
        dfs(x, y+1, cnt+1)
        dfs(x, y-1, cnt+1)
        return True
    return False

dfs(0,0,1)
print(res)