N = int(input())
directions = list(input().split(' '))

map_info = [[0 for _ in range(N+1)] for _ in range(N+1)]

# for i in range(len(map_info)):
#     print(*map_info[i])

curr_x, curr_y = 1, 1

def chk_can_go(x, y):
    if x < 1 or x > N or y < 1 or y > N:
        return False
    return True

for direction in directions:
    if direction == 'L':
        # 왼쪽으로 한칸 이동
        next_x, next_y = curr_x - 1, curr_y
    elif direction == 'R':
        # 오른쪽으로 한칸 이동
        next_x, next_y = curr_x + 1, curr_y
    elif direction == 'U':
        # 위로 한칸 이동
        next_x, next_y = curr_x, curr_y - 1
    elif direction == 'D':
        # 아래로 한칸 이동
        next_x, next_y = curr_x, curr_y + 1
        
    if chk_can_go(next_x, next_y):
        curr_x = next_x
        curr_y = next_y
    
print(curr_y, curr_x)