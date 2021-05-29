#!/usr/bin/ python
# -*- coding: utf-8 -*-
# @Time : 2021/5/29 
# @Author : XIAO
# @File : 舍弃代码.py
# 导航+打印
# def Navigation(station1,station2):
#     print(station1+'到'+station2+'轨道交通路线：')
#     l1=GetLineId(station1)
#     l2 = GetLineId(station2)
#     for ll1 in l1:
#         for ll2 in l2:
#             if ll1==ll2:
#                 way1 = GoToWay(ll1, station1, station2)
#                 print("地铁" + str(ll1) + '号线:', end='')
#                 for way in way1:
#                     print('->' + way, end='')
#                 print('(共{}站）'.format(len(way1)))
#             else:
#                 transferstation=GetTransfer(ll1,ll2)
#                 for tfs in transferstation:
#                     if(tfs!=station1):
#                         way1 = GoToWay(ll1, station1, tfs)
#                         print("地铁" + str(ll1) + '号线:', end='')
#                         for way in way1:
#                             print('->' + way, end='')
#
#                         print('(此站换乘)-> ', end='')
#
#                         way2 = GoToWay(ll2, tfs, station2)
#                         print("地铁" + str(ll2) + '号线:', end='')
#                         for i, way in enumerate(way2):
#                             print('->' + way, end='')
#                         print('  (共{}站）'.format(len(way1) + len(way2)))
#
#     print()

# 导航
# def Navigation1(station1,station2):
#     naviline=''
#     naviline+=station1+'到'+station2+'轨道交通路线：\n'
#     l1=GetLineId(station1)
#     l2 = GetLineId(station2)
#     for ll1 in l1:
#         for ll2 in l2:
#             if ll1==ll2:
#                 way1 = GoToWay(ll1, station1, station2)
#                 naviline+="地铁" + str(ll1) + '号线:'
#                 for way in way1:
#                     naviline +='->' + way
#                 naviline+='(共{}站）'.format(len(way1))+'\n'
#             else:
#                 transferstation=GetTransfer(ll1,ll2)
#                 for tfs in transferstation:
#                     way1 = GoToWay(ll1, station1, tfs)
#                     way2 = GoToWay(ll2, tfs, station2)
#                     if(way1 and way2):
#                         naviline+=('地铁' + str(ll1) + '号线:')
#                         for way in way1:
#                             naviline+='->' + way
#
#                         naviline+='(此站换乘)-> '
#                         naviline += "地铁" + str(ll2) + '号线:'
#                         for i, way in enumerate(way2):
#                             naviline += '->' + way
#                         naviline += '  (共{}站）'.format(len(way1) + len(way2)) + '\n'
#
#
#
#     return naviline
# 得到换乘站
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

# 从A到B
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
