import pyodbc
import pandas as pd
import PyQt5

# data = pd.read_sql("select Station.StationName from Rail inner join Station on Rail.StationId=Station.StationId where LineId=1", cnxn)
# cursor = cnxn.cursor()
# cursor.execute("select Station.StationName from Rail inner join Station on Rail.StationId=Station.StationId where LineId=1")
# for row in cursor:
#     print(row)

def sqllink():
    cnxn_str = ('Driver={SQL Server};'
                'Server=LAPTOP-HBNPGUI2;'
                'Database=NingboRailTransit;'
                'Trusted_Connection=yes;')
    return pyodbc.connect(cnxn_str)

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

def strline(l={}):
    strl=''
    strl+=l[0]
    for i in range(1,len(l)):
        strl+=('->'+l[i])
    return strl

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


def GetTransfer(l1,l2):
    transferstation = []
    cnxn = sqllink()
    cursor = cnxn.cursor()
    cursor.execute('''select StationName
                      from TransferStation
                    where (LineA=? and LineB=?)or(LineA=? and LineB=?)''', l1, l2, l2, l1)
    for row in cursor:
        transferstation.append(row[0])
    return transferstation

def GoToWay(line,station1,station2):
    way=[]
    StationList = Line_inquiry(line)
    start = [i for i in range(0, len(StationList)) if StationList[i] == station1]
    end = [i for i in range(0, len(StationList)) if StationList[i] == station2]
    if (start < end):
        for i in range(start[0], end[0]+1):
            way.append(StationList[i])
    if (start > end):
        for i in range(start[0] , end[0] - 1,-1):
            way.append(StationList[i])
    return way

def Navigation(station1,station2):
    print(station1+'到'+station2+'轨道交通路线：')
    l1=GetLineId(station1)
    l2 = GetLineId(station2)
    for ll1 in l1:
        for ll2 in l2:
            if ll1==ll2:
                way1 = GoToWay(ll1, station1, station2)
                print("地铁" + str(ll1) + '号线:', end='')
                for way in way1:
                    print('->' + way, end='')
                print('(共{}站）'.format(len(way1)))
            else:
                transferstation=GetTransfer(ll1,ll2)
                for tfs in transferstation:
                    way1=GoToWay(ll1,station1,tfs)
                    print("地铁"+str(ll1)+'号线:',end='')
                    for way in way1:
                        print('->'+way,end='')

                    print('(此站换乘)-> ',end='')

                    way2 = GoToWay(ll2, tfs, station2)
                    print("地铁" + str(ll2) + '号线:', end='')
                    for i,way in enumerate(way2):
                            print('->'+way,end='')
                    print('  (共{}站）'.format(len(way1)+len(way2)))
    print()


def pt(a):
    print(a)


def main():
    # station=input("按站点查询:")
    # Station_inquiry('南高教园区')
    # line=int(input("按线路查询(1,2,3……):"))
    # Line_inquiry(line)
    # Navigation('南高教园区', '慈城')
    # Navigation('儿童公园','小洋江')
    Navigation('儿童公园', '鼓楼')
    # Line_inquiry(4)

if __name__ == "__main__":
    main()