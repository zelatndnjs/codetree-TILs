n = int(input())

lines = []
for _ in range(n):
    lines.append(tuple(map(int, input().split())))

choose_line = []
answer = 0

def choose(cur_num, choose_line):
    global lines
    global answer
    if cur_num == n:
        answer = max(answer, len(choose_line))
        return
    
    chk = 0
    
    for i in choose_line:
        if not(lines[cur_num][1] < i[0] or i[1] < lines[cur_num][0]):
            chk = 1
            break
    
    if chk == 1:
        choose(cur_num + 1, choose_line)
    else:
        choose_line.append(lines[cur_num])
        choose(cur_num + 1, choose_line)
        choose_line.pop()
        choose(cur_num + 1, choose_line)
    
    return


choose(0, choose_line)

print(answer)