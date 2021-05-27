# -*- coding: utf-8 -*-
# @Time    : 2021/5/27 21:20
# @Author  : Han
# @File    : Graph.py
line={1:[1,2,3,4,5,6,7,8,9,10,11,12,13],
      2:[14,15,5,16,17],
      3:[18,19,16,20,21],
      4:[22,23,24,20,25,26,27]}
graph={}
# graph= {i:[c for c, a in enumerate(line1) ] for i in line1}
for k in range(1,5):
    for i in range(0, len(line[k]) - 1):
        graph.setdefault(line[k][i], []).append(line[k][i + 1])
        graph.setdefault(line[k][i + 1], []).append(line[k][i])
print(graph)
qianqunode={}
def printnode(s,e):
    if(e!=s):
        printnode(s,qianqunode[e])
    print(e)
def BFS(graph,s,e):#graph图  s指的是开始结点
    #需要一个队列
    queue=[]
    queue.append(s)
    seen=set()#看是否访问过该结点
    seen.add(s)
    while (len(queue)):
        vertex=queue.pop(0)#保存第一结点，并弹出，方便把他下面的子节点接入
        nodes=graph[vertex]#子节点的数组
        for w in nodes:
            if w not in seen:#判断是否访问过，使用一个数组
                queue.append(w)
                qianqunode[w]=vertex
                seen.add(w)
                if(w==e):
                    print()

BFS(graph,3,27)
print(qianqunode)
printnode(3,27)