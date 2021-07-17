import pyodbc
import pandas as pd
import PyQt5

# data = pd.read_sql("select Station.StationName from Rail inner join Station on Rail.StationId=Station.StationId where LineId=1", cnxn)
# cursor = cnxn.cursor()
# cursor.execute("select Station.StationName from Rail inner join Station on Rail.StationId=Station.StationId where LineId=1")
# for row in cursor:
#     print(row)

utilsnaviway=[]

'''
函数名:sqllinkrail()
功能:数据库连接
参数:
返回:
'''
def sqllinkrail():
    cnxn_str = ('Driver={SQL Server};'
                'Server=LAPTOP-HBNPGUI2;'
                'Database=NingboRailTransitTest;'
                'Trusted_Connection=yes;')
    return pyodbc.connect(cnxn_str)

'''
函数名:sqllinkcard()
功能:数据库连接
参数:
返回:
'''
def sqllinkcard():
    cnxn_str = ('Driver={SQL Server};'
                'Server=LAPTOP-HBNPGUI2;'
                'Database=BusCardManagement;'
                'Trusted_Connection=yes;')
    return pyodbc.connect(cnxn_str)

'''
函数名:getalllinename()
功能:获得所有路线名称
参数:
返回:
'''
def getalllinename():
    l=[]
    cnxn = sqllinkrail();
    st = pd.read_sql('''select LineName
    from Line''', cnxn)
    for stt in st["LineName"]:
        l.append(stt)
    return l

'''
函数名:GetLineNameToId
功能:路线转为编号
参数:
返回:
'''
def GetLineNameToId():
    dict = {}
    cnxn = sqllinkrail()
    cursor = cnxn.cursor()
    cursor.execute('''select LineId,LineName from Line''')
    for row in cursor:
        dict[row[1]] = row[0]
    return dict

'''
函数名:Station_inquiry
功能:站点查询
参数:
返回:
'''
def Station_inquiry(station):
    l=''
    cnxn = sqllinkrail();
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

'''
函数名:Line_inquiry
功能:路线查询
参数:
返回:
'''
def Line_inquiry(line):
    l={}
    cnxn = sqllinkrail()
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

'''
函数名:strline()
功能:文本转换
参数:
返回:
'''
def strline(l={}):
    strl=''
    strl+=l[0]
    for i in range(1,len(l)):
        strl+=('->'+l[i])
    return strl

'''
函数名:GetLineId()
功能:得到一个站的路线
参数:
返回:
'''
def GetLineId(station):
    l=[]
    cnxn = sqllinkrail()
    cursor = cnxn.cursor()
    cursor.execute('''select Line.LineId
                          from Station inner join Rail on Station.StationId=Rail.StationId inner join Line on Line.LineId=Rail.LineID
                          where Station.StationName=? ''', station)
    for row in cursor:
        l.append(row[0])
    return l

'''
函数名:GetStationId()
功能:获得站点编号
参数:
返回:
'''
def GetStationId(station):
    cnxn = sqllinkrail()
    cursor = cnxn.cursor()
    cursor.execute('''select StationId from Station
                    where StationName=? ''', station)
    for row in cursor:
        s=row[0]
    return s

'''
函数名:GetStationIdToName()
功能:得到站点序号与站名dict
参数:
返回:
'''
def GetStationIdToName():
    dict={}
    cnxn = sqllinkrail()
    cursor = cnxn.cursor()
    cursor.execute('''select StationId,StationName from Station''')
    for row in cursor:
        dict[row[0]]=row[1]
    return dict

'''
函数名:GetAllrailline()
功能:获取有哪些路线，例如1,3,8,11
参数:
返回:
'''
def GetAllrailline():
    l = []
    cnxn = sqllinkrail();
    st = pd.read_sql('''select distinct LineId from Rail''', cnxn)
    for stt in st["LineId"]:
        l.append(int(stt))
    return l

'''
函数名:getrailgraph()
功能:获得路线图
参数:
返回:
'''
def getrailgraph():
    railline=GetAllrailline()#获取有哪些路线，例如1,3,8,11
    rail={}
    graph={}
    cnxn = sqllinkrail()
    cursor = cnxn.cursor()
    cursor.execute('''select LineId,StationId from Rail''')
    for row in cursor:
        rail.setdefault(row[0], []).append(row[1])
    for k in railline:
        for i in range(0, len(rail[k]) - 1):
            graph.setdefault(rail[k][i], []).append([rail[k][i + 1], k])
            graph.setdefault(rail[k][i + 1], []).append([rail[k][i], k])
    return graph

'''
函数名:BFS()
功能:BFS
参数:
返回:
'''
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

'''
函数名:printnode
功能:前驱结点回溯
参数:
返回:
'''
def printnode(s, e, l,qianqunode):
    dict=GetStationIdToName()
    if (e != s):
        printnode(s, qianqunode[e][0], qianqunode[e][1],qianqunode)
    utilsnaviway.append([dict[e], l])

'''
函数名:Navigation()
功能:导航，最短路径
参数:
返回:
'''
def Navigation(ststion1,station2):
    graph=getrailgraph()
    startid=GetStationId(ststion1)
    endid=GetStationId(station2)
    q=BFS(graph, startid, endid)
    utilsnaviway.clear()
    printnode(startid,endid,0,q)

'''
函数名:UpdateCardRecord()
功能:更新乘车记录
参数:
返回:
'''
def UpdateCardRecord(card,balance,cost,s,e):
    cnxn = sqllinkcard();
    cursor = cnxn.cursor()
    cursor.execute('''UPDATE Card SET Balance = ? WHERE CardNumber = ? ''', balance,card)
    waystr=''
    waystr=s+'->'+e
    cursor.execute('''INSERT INTO CardRecord VALUES (?,?,(select CONVERT(varchar, getdate(), 120 )),?)''',card,waystr,cost)
    cnxn.commit()
    return

'''
函数名:Cardisexist()
功能:判断卡号是否存在
参数:
返回:
'''
def Cardisexist(cardnum):
    l=[]
    cnxn = sqllinkcard();

    cursor = cnxn.cursor()
    cursor.execute('''select isnull((select top(1) 1 from Card where CardNumber=?), 0) ''', cardnum)
    for row in cursor:
        l.append(row[0])
    # return l
    if(l[0]==1):
        return True
    return False

'''
函数名:Cardquery()
功能:查询卡内容
参数:
返回:
'''
def Cardquery(cardnum):
    l=[]
    cnxn = sqllinkcard();

    cursor = cnxn.cursor()
    cursor.execute('''select CardType,Balance from Card where CardNumber=?''', cardnum)
    for row in cursor:
        l.append(row)
    return l

'''
函数名:Cardquery()
功能:管理路线
参数:
返回:
'''
def updateline(data):
    l=[]
    lnew=[]
    cnxn = sqllinkrail()
    cursor = cnxn.cursor()
    cursor.execute(
        '''select isnull((select top(1) 1 from Line where LineId=?), 0)''', int(data[0][1]))
    for row in cursor:
        flag = row[0]
    if (flag == 0):
        linename = '轨道交通' + str(data[0][1]) + '号线'
        cursor = cnxn.cursor()
        cursor.execute('''insert into Line values(?,?)''', int(data[0][1]), linename)
        cnxn.commit()
    linedata = pd.read_sql("select * from Station", cnxn)
    count=len(linedata)
    for i in linedata['StationName']:
        l.append(i)
    for i in data[1]:
        if(i not in l):
            count+=1
            lnew.append((count,i))
    for station in lnew:
        cursor = cnxn.cursor()
        cursor.execute('''insert into Station VALUES (?,?) ''', station[0],station[1])
        cnxn.commit()
    for i in data[1]:
        print(data[0][1],i)
        cursor = cnxn.cursor()
        cursor.execute('''insert into Rail (LineId,StationId) VALUES (?,(select StationId from Station where StationName=?))''',int(data[0][1]),i)
        cnxn.commit()



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

# if __name__ == "__main__":
#     main()