S = input()

total = 0
for s in S:
    tmp_s = int(s)
    if tmp_s <= 1 or total == 0:
        total += tmp_s
    else:
        total *= tmp_s
        
print(total)