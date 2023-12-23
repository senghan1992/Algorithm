# nums = list(map(int, input().split()))
# # print(nums)
# nums.sort()
# # print(nums)
# cnt = 0
# for n in nums:
#     if len(nums[1:]) > n-1:
#         for i in range(n):
#             nums.pop(0)
#         cnt += 1
        
# print(cnt)

n = int(input())
data = list(map(int, input().split()))
data.sort()

result = 0  # 총 그룹의 개수
count = 0   # 현재 그룹에 포함된 모험가의 수

for i in data:      # 공포도를 낮은 순으로 하나씩 확인하며
    count += 1      # 현재 그룹에 해당 모험가를 포함
    if count >= i:  # 총 그룹의 수 증가시키기
        result += 1
        count = 0
        
print(result)