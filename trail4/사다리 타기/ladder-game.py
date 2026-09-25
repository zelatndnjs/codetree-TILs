n,m = map(int, input().split())

edges = [tuple(map(int,input().split())) for i in range(m)]

def result(n, edges):
    sorted_edges = sorted(edges, key=lambda x:x[1])
    people = [i for i in range(1, n+1)]
    for edge in sorted_edges:
        tmp = people[edge[0]-1]
        people[edge[0]-1] = people[edge[0]]
        people[edge[0]] = tmp
    return people


answer_list = result(n, edges)
answer = m

choose_edge = []
cur_num = 0

def choose(n, edges, choose_edge, cur_num):
    global answer
    if cur_num == m:
        if answer_list == result(n, choose_edge):
            if answer > len(choose_edge):
                answer = len(choose_edge)
        return
    if answer_list == result(n, choose_edge):
        if answer > len(choose_edge):
            answer = len(choose_edge)
            return
    choose_edge.append(edges[cur_num])
    choose(n, edges, choose_edge, cur_num+1)
    choose_edge.pop()
    choose(n, edges, choose_edge, cur_num+1)

choose(n, edges, choose_edge, cur_num)

print(answer)