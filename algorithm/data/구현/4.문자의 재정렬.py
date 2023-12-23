S = input()

str_list = []
cnt = 0
for s in S:
    if s.isdigit():
        cnt += int(s)
    else:
        str_list.append(s)

print(f"{''.join(sorted(str_list))}{str(cnt)}")