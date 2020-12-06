# coding: utf-8
from cvxpy import *
import numpy as np
import cvxpy as cvx
import pandas as pd
from matplotlib import pyplot as plt


def moving_average(sample, window_size=7):
    for i in range(0, window_size):
        sample.iloc[i] = np.mean(sample[:i + 1])
    for i in range(window_size + 1, len(sample.index)):
        sample.iloc[i] = (sample.iloc[i - 1] * (window_size - 1) + sample.iloc[i]) / window_size
    return sample




# Unit cost of PV panel: Cs USD/(kW day) 2025
# Unit cost of battery: Cb USD/(kWh day) 900
# Unit cost of transformer: Cts USD/(kW day) 788
# Unit cost of charger cost: Cchg USD/(kW day) 500
Cs, Cb, Cts, Cchg = 2025, 900, 788, 500
n = 120
# Electricity price purchase: Cg(k) USD/(kW day) 7~19: 0.22*6, 0.44*6
# Electricity price sell: Cg, fb(k) USD/(kW day) 7~19: 0.1
# Charging price for EV: Cev 7~19: 0.24*6, 0.48*6
# Cgp = np.array([0.22,0.22,0.22,0.22,0.22,0.22,0.44,0.44,0.44,0.44,0.44,0.44])
Cg = np.ones(n)*0.4
Cgs = np.ones(n)*0.3
Cev = np.ones(n)*2
# Cev = np.array([0.24,0.24,0.24,0.24,0.24,0.24,0.48,0.48,0.48,0.48,0.48,0.48])

# Problem data.
data = pd.read_csv('opti.csv')
Ppv = data['Ppv'].values
Pl = data['Pcharge'].values
P = Pl-Ppv
plt.plot(np.arange(n), Ppv)
plt.plot(np.arange(n), moving_average(pd.DataFrame(Ppv)).values)
plt.show()

np.random.seed(1)
# Construct the problem.
grid = cvx.Variable(n)
battery = cvx.Variable(n)
battery_energy = 900 # kwh
objective = cvx.Minimize(-sum(grid*Cg)-sum(Pl*Cev)) ## 最后一项是晚上grid给电池充电，这时候的电价是0.25， 白天的电价是0.5，用cgs已经表示了
# Battery size b 0.1*1000-0.9*1000kW
# Grid size s -125-125kW
# Alpha 0.9


# relationship between temporal electricity power of ['Grid','Battery','PV', 'Demand']
constraints = [grid+battery == P,
               sum(battery) == 0,
               ## constraint on the energy of battery
               -0.5*1000 <= battery, battery <= 0.5*1000,
               -125 <= grid, grid <= 125]
for i in range(n+1):
    constraints += [-800 <= sum(battery[0:i]), sum(battery[0:i]) <= 0]

# for i in range(0, n+1, 5):
#     constraints += [-800 <= sum(battery[i:i+5])/5, sum(battery[i:i+5])/5 <= 0]
prob = cvx.Problem(objective, constraints)
print('Without pv', np.dot(Pl,Cg) - np.dot(Pl, Cev))
print("With pv", prob.solve())
print("Battery_remain", battery_energy + np.sum(battery.value)/5)
result = np.column_stack((grid.value, battery.value))
result = pd.DataFrame(np.column_stack((result, Ppv)))
result = pd.DataFrame(np.column_stack((result, Pl)))
result.to_csv('result.csv', header=['Grid','Battery','PV', 'Demand'])
plt.plot(np.arange(n), grid.value, np.arange(n), battery.value, np.arange(n), Ppv, np.arange(n), Pl)
plt.legend(['Grid','Battery','PV', 'Demand'])
plt.show()

# relationship of earnings between PV and noPV
price_withoutev = Pl*Cg - Pl*Cev
price_withev = grid.value*Cg - Pl*Cev
price_noPV = []
price_opti = []
price_noPV.append(np.abs(price_withoutev[0]))
price_opti.append(np.abs(price_withev[0]))
for i in range(1, n):
    price_noPV.append(np.abs(np.sum(price_withoutev[0:i])))
    price_opti.append(np.abs(np.sum(price_withev[0:i])))
plt.figure()
plt.plot(np.arange(n), np.array(price_noPV))
plt.plot(np.arange(n), np.array(price_opti))
plt.legend(['price_noPV', 'price_opti'])
plt.show()
print('price_noPV: ',price_noPV[n-1], 'USD')
print('price_opti: ', price_opti[n-1], 'USD')

# relationship of overall electricity use between PV and noPV
# grid_noPV = []
# grid_opti = []
# grid_noPV.append(Pl[0])
# grid_opti.append(grid.value[0])
# for i in range(4, n, 5):
#     grid_noPV.append(np.sum(Pl[0:i])/(i+1))
#     grid_opti.append(np.sum(grid.value[0:i])/(i+1))
# plt.figure()
# plt.plot(np.arange(25), np.array(grid_noPV))
# plt.plot(np.arange(25), np.array(grid_opti))
# plt.legend(['Electricity_usage_withoutPV', 'Electricity_usage_withPV'])
# plt.show()
# print('Electricity_usage_withoutPV', grid_noPV[23], 'KWh', 'Electricity_usage_withPV', grid_opti[23], 'KWh')

# relationship of battery w.r.t. time
battery_result = np.zeros(n)
for i in range(n):
    battery_result[i] = battery.value[i]/5
battery_sum = np.zeros(n)
for i in range(n):
    battery_sum[i] = 900 + np.sum(battery_result[0:i])
print('remaining_battery:', battery_sum)
plt.figure()
plt.plot(np.arange(n), np.array(battery_sum))
plt.show()

