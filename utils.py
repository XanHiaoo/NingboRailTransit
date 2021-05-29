import pyodbc
import pandas as pd
import PyQt5

# data = pd.read_sql("select Station.StationName from Rail inner join Station on Rail.StationId=Station.StationId where LineId=1", cnxn)
# cursor = cnxn.cursor()
# cursor.execute("select Station.StationName from Rail inner join Station on Rail.StationId=Station.StationId where LineId=1")
# for row in cursor:
#     print(row)

utilsnaviway=[]
#数据库连接
def sqllink():
    cnxn_str = ('Driver={SQL Server};'
                'Server=LAPTOP-HBNPGUI2;'
                'Database=NingboRailTransit;'
                'Trusted_Connection=yes;')
    return pyodbc.connect(cnxn_str)

#获得所有路线返回一个列表
def getalllinename():
    l=[]
    cnxn = sqllink();
    st = pd.read_sql('''select LineName
    from Line''', cnxn)
    for stt in st["LineName"]:
        l.append(stt)
    return l

def GetLineNameToId():
    dict = {}
    cnxn = sqllink()
    cursor = cnxn.cursor()
    cursor.execute('''select LineId,LineName from Line''')
    for row in cursor:
        dict[row[1]] = row[0]
    return dict

#站点查询
def Station_inquiry(station):
    l=''
    cnxn = sqllink();
    st = pd.read_sql('''select StationName
        from Station''', cnxn)
    for stt in st['StationName']:
        if station == stt:
            cursor = cnxn.cursor()
            cursor.execute('''select Line.LineName
                              from Line inner join Rail on Line.LineId=Rail.LineId inner join Station on Station.StationId=Rail.StationId
                              where Station.StationName=? ''', station)
            for row in cursor:
                l+=str(row[0])+'\n'
            return l
    else:
        return '没有这个站'

# 路线查询
def Line_inquiry(line):
    l={}
    cnxn = sqllink()
    li = pd.read_sql('''select LineId
                        from Line''', cnxn)
    for lii in li['LineId']:
        if line == lii:
            cursor = cnxn.cursor()
            cursor.execute('''select Station.StationName
                        from Rail inner join Station on Rail.StationId=Station.StationId
                        where LineId=?''', int(line))
            for i,row in enumerate(cursor):
                # print(row[0])
                l[i]=row[0]
            return l
    return

# 文本转化
def strline(l={}):
    strl=''
    strl+=l[0]
    for i in range(1,len(l)):
        strl+=('->'+l[i])
    return strl

# 得到一个站的路线
def GetLineId(station):
    l=[]
    cnxn = sqllink()
    cursor = cnxn.cursor()
    cursor.execute('''select Line.LineId
                          from Station inner join Rail on Station.StationId=Rail.StationId inner join Line on Line.LineId=Rail.LineID
                          where Station.StationName=? ''', station)
    for row in cursor:
        l.append(row[0])
    return l

def GetStationId(station):
    cnxn = sqllink()
    cursor = cnxn.cursor()
    cursor.execute('''select StationId from Station
                    where StationName=? ''', station)
    for row in cursor:
        s=row[0]
    return s

# 得到站点序号与站名dict
def GetStationIdToName():
    dict={}
    cnxn = sqllink()
    cursor = cnxn.cursor()
    cursor.execute('''select StationId,StationName from Station''')
    for row in cursor:
        dict[row[0]]=row[1]
    return dict

#获取有哪些路线，例如1,3,8,11
def GetAllrailline():
    l = []
    cnxn = sqllink();
    st = pd.read_sql('''select distinct LineId from Rail''', cnxn)
    for stt in st["LineId"]:
        l.append(int(stt))
    return l

# 获得路线图
def getrailgraph():
    railline=GetAllrailline()#获取有哪些路线，例如1,3,8,11
    rail={}
    graph={}
    cnxn = sqllink()
    cursor = cnxn.cursor()
    cursor.execute('''select LineId,StationId from Rail''')
    for row in cursor:
        rail.setdefault(row[0], []).append(row[1])
    for k in railline:
        for i in range(0, len(rail[k]) - 1):
            graph.setdefault(rail[k][i], []).append([rail[k][i + 1], k])
            graph.setdefault(rail[k][i + 1], []).append([rail[k][i], k])
    return graph

#BFS
def BFS(graph, s, e):  # graph图  s指的是开始结点
    qianqunode = {}
    queue = []
    queue.append(s)
    seen = set()  # 看是否访问过该结点
    seen.add(s)
    while (len(queue)):
        vertex = queue.pop(0)  # 保存第一结点，并弹出，方便把他下面的子节点接入
        nodes = graph[vertex]  # 子节点的数组
        for w in nodes:
            if w[0] not in seen:  # 判断是否访问过，使用一个数组
                queue.append(w[0])
                qianqunode[w[0]] = [vertex, w[1]]
                seen.add(w[0])
                if (w[0] == e):
                    print()

    return qianqunode

#前驱结点回溯
def printnode(s, e, l,qianqunode):
    dict=GetStationIdToName()
    if (e != s):
        printnode(s, qianqunode[e][0], qianqunode[e][1],qianqunode)
    utilsnaviway.append([dict[e], l])

#bfs导航，最短路径
def Navigation(ststion1,station2):
    graph=getrailgraph()
    startid=GetStationId(ststion1)
    endid=GetStationId(station2)
    q=BFS(graph, startid, endid)
    utilsnaviway.clear()
    printnode(startid,endid,0,q)


def main():
    return
    # station=input("按站点查询:")
    # Station_inquiry('南高教园区')
    # line=int(input("按线路查询(1,2,3……):"))
    # Line_inquiry(line)
    # Navigation('南高教园区', '慈城')
    # Navigation('儿童公园','小洋江')
    # Navigation('儿童公园', '鼓楼')
    # Line_inquiry(4)

if __name__ == "__main__":
    main()