import numpy as np
import random
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns  # 用于合并绘图

# 定义车辆信息数据框和属性
df_Vehicle = pd.DataFrame(columns=('vehicleID',  # 车辆id
                                   'mode',  # 车辆类型，0普通车辆，1电动车（不需要充电）2电动车正常充电3电动车占用充电桩当做停车位
                                   'pkID',  # 停车场id
                                   'arrTime',  # 车辆到达时间，以分钟为单位，将8:00~20:00分成780个时间点
                                   'pkStatus', ### 新增属性，是否已经进入停车场,0未进入，1在停车场，2离开停车场
                                   'entPkTime',  # 进入车位时间
                                   'pkSpaceID',  # 进入车位编号
                                   'stayTime',  # 停车时间
                                   'depTime',  # 离开车位时间
                                   'reservedTime', ### 驻留时间
                                   'inQueque', ### 新增属性，是否在排队
                                   'waitingTime'  # 等待时间
                                   ))
# 定义停车位信息数据框和属性
df_ParkingSpace = pd.DataFrame(columns=('pkSpaceID',  # 停车位编号
                                        'pkID',  # 停车场编号
                                        'typePkMode',  # 停车场类型, 0普通停车场，1充电桩停车场
                                        'pksAvailable',  # 当前是否可用
                                        'inusedTimes',  # 累计使用次数
                                        'accInusedTime',  # 累计使用时间
                                        'reservedTime',  # 剩余使用时间
                                        'vehIDSeries'  # 使用过的车辆编号
                                        ))
# 定义停车场信息数据框和属性
df_Parkinglot = pd.DataFrame(columns=('pkID',  # 停车场编号
                                      'typePkMode',  # 停车场类型
                                      'numPkSpace',  # 停车场车位数
                                      'timePnt',  # 时间节点
                                      'initPkOcc',  # 初始已使用车位数
                                      '_0curPkOcc',  # 当前使用车辆数
                                      '_0queLength'  # 排队车辆数
                                      ))

# 停车场初始化，普通停车位，已使用普通停车位，充电桩，已使用充电桩
'''
这里有个问题，充电桩占车位比例差异较大，如果按照各个停车场电动车停放比例一致来考虑，
则部分充电桩可能会排队较长。当然，这也可以用来测试充电桩布局均匀的重要性。
'''

# 第一列普通停车位车位数，第二列初始占用普通停车位
# 第三列充电停车位，第三列初始占用充电停车位
parkingIndex = [[53, 34, 8, 2],
                [150, 22, 8, 2],
                [54, 34, 6, 2],
                [57, 15, 3, 1],
                [140, 44, 10, 3]]

# 车辆初始化
# 各时段到达车辆分布，需要结合调查值做修正
park_arr = [[19, 9, 8, 9, 8, 8, 2, 1, 3, 3, 1, 2, 2],
            [19, 11, 7, 10, 10, 5, 1, 7, 3, 2, 4, 2, 2],
            [17, 9, 11, 10, 11, 7, 3, 4, 2, 5, 3, 3, 3],
            [14, 11, 12, 11, 11, 3, 8, 5, 4, 2, 4, 2, 2],
            [12, 9, 6, 8, 10, 10, 2, 3, 4, 3, 2, 2, 3]]

ev_rat = 0.2  # 电动车比例
ev_charge = 0.5  # 需要充电的电动车占比
ev_charge_illegal = 0.2  # 使用充电桩作为常规车位车辆占比
pv_pks = 0.3  # pv 车位所占比例

average_charge_time = 30  # 单位：分钟
average_parking_time = 240  # 单位：分钟； 已废弃，使用调查值。

stayTime = [507, 399, 509, 400, 430]  # 每个停车场的平均停留时间，单位：分钟

vehNum = 0
pkSpaceNum = 0

# 停车位初始化与车辆初始编号
# 辅助计数变量
j = 0
for i in range(5):
    # 普通车位初始化
    for k in range(parkingIndex[i][0]):
        df_ParkingSpace = df_ParkingSpace.append([{'pkSpaceID': pkSpaceNum + k + 1,
                                                   'pkID': str(i + 1) + 'a',
                                                   'typePkMode': 0,
                                                   'pksAvailable': 1,
                                                   'inusedTimes': 0,
                                                   'accInusedTime': 0,
                                                   'reservedTime': 0,
                                                   'vehIDSeries': ''}], ignore_index=True)

    normalParkingSpaceListOcc = random.sample(list(range(parkingIndex[i][0])), parkingIndex[i][1])
    for k in normalParkingSpaceListOcc:
        j = j + 1
        _staytime = np.random.poisson(lam=stayTime[i])
        df_ParkingSpace.loc[df_ParkingSpace.pkSpaceID == pkSpaceNum + k + 1, 'inusedTimes'] = 1
        df_ParkingSpace.loc[df_ParkingSpace.pkSpaceID == pkSpaceNum + k + 1, 'pksAvailable'] = 0
        df_ParkingSpace.loc[df_ParkingSpace.pkSpaceID == pkSpaceNum + k + 1, 'reservedTime'] = _staytime
        df_ParkingSpace.loc[df_ParkingSpace.pkSpaceID == pkSpaceNum + k + 1, 'vehIDSeries'] += str(vehNum + j)

        df_Vehicle = df_Vehicle.append([{'vehicleID': vehNum + j, # 车辆编号
                                         'mode': 0,
                                         'pkID': str(i + 1) + 'a',
                                         'arrTime': 0,
                                         'pkStatus': 1,
                                         'entPkTime': 0,
                                         'pkSpaceID': pkSpaceNum + k + 1,
                                         'stayTime': _staytime,
                                         'reservedTime':_staytime,
                                         'depTime': _staytime,
                                         'inQueque': 0,
                                         'waitingTime': 0
                                         }], ignore_index=True
                                       )
    pkSpaceNum += parkingIndex[i][0]

    # 充电桩停车位初始化
    for k in range(parkingIndex[i][2]):
        if k < int(parkingIndex[i][2]*pv_pks):
            pvSta = 1
        else:
            pvSta = 2

        df_ParkingSpace = df_ParkingSpace.append([{'pkSpaceID': pkSpaceNum + k + 1,
                                                   'pkID': str(i + 1) + 'b',
                                                   'typePkMode': pvSta,  # pv充电桩1， 普通充电桩2
                                                   'pksAvailable': 1,
                                                   'inusedTimes': 0,
                                                   'accInusedTime': 0,
                                                   'reservedTime': 0,
                                                   'vehIDSeries':'' }], ignore_index=True)

    evParkingSpaceListOcc = random.sample(list(range(parkingIndex[i][2])), parkingIndex[i][3])
    for k in evParkingSpaceListOcc:
        j = j + 1
        _staytime = np.random.poisson(lam=stayTime[i])
        df_ParkingSpace.loc[df_ParkingSpace.pkSpaceID == pkSpaceNum + k + 1, 'inusedTimes'] = 1
        df_ParkingSpace.loc[df_ParkingSpace.pkSpaceID == pkSpaceNum + k + 1, 'pksAvailable'] = 0
        df_ParkingSpace.loc[df_ParkingSpace.pkSpaceID == pkSpaceNum + k + 1, 'reservedTime'] = _staytime
        df_ParkingSpace.loc[df_ParkingSpace.pkSpaceID == pkSpaceNum + k + 1, 'vehIDSeries'] += str(vehNum + j)

        df_Vehicle = df_Vehicle.append([{'vehicleID': vehNum + j,
                                         'mode': 2,
                                         'pkID': str(i + 1) + 'b',
                                         'arrTime': 0,
                                         'pkStatus': 1,
                                         'entPkTime': 0,
                                         'pkSpaceID': pkSpaceNum + k + 1,
                                         'stayTime': _staytime,
                                         'reservedTime': _staytime,
                                         'depTime': _staytime,
                                         'inQueque': 0,
                                         'waitingTime': 0
                                         }], ignore_index=True
                                       )

    pkSpaceNum += parkingIndex[i][2]
    # vehNum += parkingIndex[i][1]
    # vehNum += parkingIndex[i][3]

for i in range(5):
    vehNum += parkingIndex[i][1]
    vehNum += parkingIndex[i][3]

# 辅助变量，统计车位数
n = 0
# 随机生成车辆，对车辆分配车辆类型、停车场、车辆达到时间和停车时间等属性。
for i in range(5):
    park_arr_timeid = []
    ev_sample = []
    ev_sample_illegal = []

    # 把小时划分为分钟
    time_0 = list(range(60))
    for j in range(13):
        # 按照到达的车辆数，在每个小时的60个数字进行有放回的抽样，因为可能存在多辆车同时到达的情形。
        # 0～60 抽，60～120抽
        temp_arr = np.random.choice(time_0, park_arr[i][j], replace=True) + 60 * j + 1
        # 合并成为一个停车到达时间序列
        park_arr_timeid.extend(temp_arr)

    # 对停车到达时间序列进行排序
    park_arr_timeid.sort()

    # 获取电动车辆编号
    ev_sample_id = random.sample(list(range(len(park_arr_timeid))), int(len(park_arr_timeid) * ev_rat))
    ev_sample_id.sort()

    # 获取需充电车辆编号；这里按全日到达车辆来抽样电动车辆，避免很多小时电动车到达为0.
    ev_sample_id_normal = random.sample(ev_sample_id, int(len(ev_sample_id) * ev_charge))
    ev_sample_id_normal.sort()

    # 获使用充电桩当做普通停车位的车辆编号
    ev_sample_id_illegal = random.sample(ev_sample_id_normal, int(len(ev_sample_id_normal) * ev_charge_illegal))
    ev_sample_id_illegal.sort()

    # 车辆初始化
    ## 普通停车位
    for k in range(len(park_arr_timeid)):
        if k not in ev_sample_id_normal:
            n += 1
            df_Vehicle = df_Vehicle.append([{'vehicleID': vehNum + n,
                                             'mode': 0,
                                             'pkID': str(i + 1) + 'a',
                                             'arrTime': park_arr_timeid[k],
                                             'pkStatus': 0,
                                             'stayTime': np.random.poisson(lam=stayTime[i]),
                                             'waitingTime':0
                                             }], ignore_index=True)

    ## 正常充电停车车辆
    for k in ev_sample_id_normal:
        if k not in ev_sample_id_illegal:
            n += 1
            df_Vehicle = df_Vehicle.append([{'vehicleID': vehNum + n,
                                             'mode': 2,
                                             'pkID': str(i + 1) + 'b',
                                             'arrTime': park_arr_timeid[k],
                                             'pkStatus': 0,
                                             'stayTime': np.random.poisson(lam=average_charge_time),
                                             'waitingTime':0
                                             }], ignore_index=True)

    ## 使用充电车位作为普通停车位车辆
    for k in ev_sample_id_illegal:
        n += 1
        df_Vehicle = df_Vehicle.append([{'vehicleID': vehNum + n,
                                         'mode': 3,
                                         'pkID': str(i + 1) + 'b',
                                         'arrTime': park_arr_timeid[k],
                                         'pkStatus': 0,
                                         'stayTime': np.random.poisson(lam=stayTime[i]),
                                         'waitingTime':0
                                         }], ignore_index=True)

for i in range(5):
    for j in ['a', 'b']:
        if j == 'a':
            df_Parkinglot = df_Parkinglot.append([{'pkID': str(i + 1) + j,
                                                   'typePkMode': 0,
                                                   'numPkSpace': parkingIndex[i][0],
                                                   'timePnt': 0,
                                                   'initPkOcc': parkingIndex[i][1],
                                                   '_0curPkOcc': parkingIndex[i][1],
                                                   '_0queLength': 0
                                                   }], ignore_index=True)
        if j == 'b':
            df_Parkinglot = df_Parkinglot.append([{'pkID': str(i + 1) + j,
                                                   'typePkMode': 1,
                                                   'numPkSpace': parkingIndex[i][2],
                                                   'timePnt': 0,
                                                   'initPkOcc': parkingIndex[i][3],
                                                   '_0curPkOcc': parkingIndex[i][3],
                                                   '_0queLength': 0
                                                   }], ignore_index=True)

# 停车仿真

# 对车辆按照到达时间进行排序
df_Vehicle = df_Vehicle.sort_values(by='arrTime')
vehNum = len(df_Vehicle)

curRec = 0
for i in range(780):

    hour = int(i / 60) + 8
    minutes = i - 60 * (hour -8)

    if i % 5 == 0:
        print("-----running %02d 时 %02d 分-----" %(hour, minutes))

    # # 停车场信息初始化
    lastOcc = '_' + str(i) + 'curPkOcc'
    lastQueLen = '_' + str(i) + 'queLength'

    df_Parkinglot_iter = df_Parkinglot.loc[:,['pkID',lastOcc,lastQueLen]]

    for k in range(vehNum):

        if df_Vehicle.iloc[k, df_Vehicle.columns.get_loc('arrTime')] <= i:
            # 过滤掉初始入库车辆
            # 已入库
            if df_Vehicle.iloc[k, df_Vehicle.columns.get_loc('pkStatus')] == 1:

                # 更新已入库车辆信息
                df_Vehicle.iloc[k, df_Vehicle.columns.get_loc('reservedTime')] -= 1

                # 更新停车位信息
                df_ParkingSpace.loc[df_ParkingSpace.pkSpaceID == df_Vehicle.iloc[
                    k, df_Vehicle.columns.get_loc('pkSpaceID')], 'accInusedTime'] += 1
                df_ParkingSpace.loc[df_ParkingSpace.pkSpaceID == df_Vehicle.iloc[
                    k, df_Vehicle.columns.get_loc('pkSpaceID')], 'reservedTime'] -= 1

                # 更新停车场临时信息
                if df_Vehicle.iloc[k, df_Vehicle.columns.get_loc('reservedTime')] == 0:
                    df_ParkingSpace.loc[df_ParkingSpace.pkSpaceID == df_Vehicle.iloc[
                        k, df_Vehicle.columns.get_loc('pkSpaceID')], 'pksAvailable'] = 1
                    df_Vehicle.loc[df_Vehicle.reservedTime == 0, 'pkStatus'] = 2
                    df_Parkinglot_iter.loc[
                        df_Parkinglot_iter.pkID == df_Vehicle.iloc[k, df_Vehicle.columns.get_loc('pkID')], lastOcc] -= 1
            # 刚刚到达
            elif df_Vehicle.iloc[k, df_Vehicle.columns.get_loc('pkStatus')] == 0:

                # 获取当前车辆车辆
                vhID = df_Vehicle.iloc[k, df_Vehicle.columns.get_loc('vehicleID')]

                # 更新待入库车辆信息
                # 建立可使用车位集
                listAvParking_df = df_ParkingSpace[
                    (df_ParkingSpace.pksAvailable == 1) & (
                                df_ParkingSpace.pkID == df_Vehicle.iloc[k, df_Vehicle.columns.get_loc('pkID')])]

                listAvParking = listAvParking_df['pkSpaceID'].values.tolist()

                if len(listAvParking):

                    newArrival = random.sample(listAvParking, 1)
                    newArrival = newArrival[0]

                    # print(newArrival)

                    # update parkingspace info
                    df_ParkingSpace.loc[df_ParkingSpace.pkSpaceID == newArrival, 'pksAvailable'] = 0
                    df_ParkingSpace.loc[df_ParkingSpace.pkSpaceID == newArrival, 'inusedTimes'] += 1
                    df_ParkingSpace.loc[df_ParkingSpace.pkSpaceID == newArrival, 'vehIDSeries'] +=(',' + str(vhID))
                    df_ParkingSpace.loc[df_ParkingSpace.pkSpaceID == newArrival, 'reservedTime'] = \
                        df_Vehicle.iloc[k, df_Vehicle.columns.get_loc('stayTime')]

                    # 更新车辆信息
                    df_Vehicle.iloc[k, df_Vehicle.columns.get_loc('entPkTime')] = i
                    df_Vehicle.iloc[k, df_Vehicle.columns.get_loc('pkStatus')] = 1
                    df_Vehicle.iloc[k, df_Vehicle.columns.get_loc('reservedTime')] = \
                        df_Vehicle.iloc[k, df_Vehicle.columns.get_loc('stayTime')]
                    df_Vehicle.iloc[k, df_Vehicle.columns.get_loc('pkSpaceID')] = newArrival
                    df_Vehicle.iloc[k, df_Vehicle.columns.get_loc('depTime')] = i + df_Vehicle.iloc[k, df_Vehicle.columns.get_loc('stayTime')]

                    #更新停车库信息
                    if df_Vehicle.iloc[k, df_Vehicle.columns.get_loc('inQueque')] == 1:
                        df_Parkinglot_iter.loc[df_Parkinglot_iter.pkID == df_Vehicle.iloc[k, df_Vehicle.columns.get_loc('pkID')], lastOcc] += 1
                        df_Parkinglot_iter.loc[df_Parkinglot_iter.pkID == df_Vehicle.iloc[
                            k, df_Vehicle.columns.get_loc('pkID')], lastQueLen] -= 1
                    else:
                        df_Parkinglot_iter.loc[df_Parkinglot_iter.pkID == df_Vehicle.iloc[k, df_Vehicle.columns.get_loc('pkID')], lastOcc] += 1

                else:
                    # 更新车辆信息
                    df_Vehicle.iloc[k, df_Vehicle.columns.get_loc('inQueque')] = 1
                    df_Vehicle.iloc[k, df_Vehicle.columns.get_loc('waitingTime')] += 1

                    if df_Vehicle.iloc[k, df_Vehicle.columns.get_loc('arrTime')] == i:
                        #更新停车场信息
                        df_Parkinglot_iter.loc[df_Parkinglot_iter.pkID == df_Vehicle.iloc[k, df_Vehicle.columns.get_loc('pkID')], lastQueLen] += 1

        # 进入车辆选择
        else:
            break

    # 更新停车库信息
    curOcc = '_' + str(i + 1) + 'curPkOcc'
    curQueLen = '_' + str(i + 1) + 'queLength'

    df_Parkinglot_iter.rename(columns={lastOcc: curOcc, lastQueLen: curQueLen}, inplace=True)

    df_Parkinglot = pd.merge(df_Parkinglot, df_Parkinglot_iter, on='pkID', how='inner')

# 输出结果文件
outputfile1 = "01vehicle_record.csv"
df_Vehicle.to_csv(outputfile1, sep=',', header=True, index=False)

outputfile2 = "02parkingSpace_record.csv"
df_ParkingSpace.to_csv(outputfile2, sep=',', header=True, index=False)

outputfile3 = "03parkinglot_record.csv"
df_Parkinglot.to_csv(outputfile3, sep=',', header=True, index=False)

print('----------- simulation progress finished -----------')
