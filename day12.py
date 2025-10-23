# # Bingo-Online Lottery Game
# # vals=[-10,-7,-3,4,2]
# # vals.sort()
# # prod1=vals[-1]*vals[-2]
# # prod2=vals[0]*vals[1]
# # if prod2>prod1:
# #     print(vals[0]+vals[1])
# # else:
# #     print(vals[-1]+vals[-2])


# # Digital secure data transfer solution
# # s1='abcdefghijklmnopqrstuvwxyz'
# # s2='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# # k=3
# # ch='D'
# # if ch in s1:
# #     idx=s1.index(ch)
# #     out=s1[(idx+k)%26]
# # elif ch in s2:
# #     idx=s2.index(ch)
# #     out=s2[(idx+k)%26]
# # else:
# #     out=ch
# # print(out)


# # Pooled cab service
# # num,start,end=map(int,input().split())
# # values=list(map(int,input().split()))
# # low=min(start,end)
# # high=max(start,end)
# # ans=[]
# # for num in values:
# #     if low<=num<=high:
# #         ans.append(num)
# # print(ans)


# # Graphs
# # from collections import defaultdict
# # edges=[['A','B'],['B','D'],['A','C'],['C','E'],['E','F']]
# # adj_list=defaultdict(list)
# # for u,v in edges:
# #     adj_list[u].append(v)
# #     adj_list[v].append(v)
# # print(adj_list)


# # BFS traversal using graphs
# def BFS(graph,start):
#     visited=set()
#     q=[start]
#     while q:
#         n=q.pop(0)
#         if n not in visited:
#             print(n,end=" ")
#             visited.add(n)
#             q.extend(graph[n])
# graph={
#     'A':['B','C'],
#     'B':['A','D','E'],
#     'C':['A','F'],
#     'D':['B'],
#     'E':['B','F'],
#     'F':['C','E']    
# }
# BFS(graph,'A')


#DFS traversal
def DFS(graph,n,visited=set()):
    if n not in visited:
        print(n,end=" ")
        visited.add(n)
        for i in graph[n]:
            DFS(graph,i,visited)
graph={
    'A':['B','C'],
    'B':['A','D','E'],
    'C':['A','F'],
    'D':['B'],
    'E':['B','F'],
    'F':['C','E']    
}
DFS(graph,'A')
