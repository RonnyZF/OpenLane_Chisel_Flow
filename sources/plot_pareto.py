import csv
import numpy as np
import matplotlib.pyplot as plt
#from scipy.stats import pareto
import oapackage


def pareto_frontier(Xs, Ys, Zs, maxX = True, maxY = True):
# Sort the list in either ascending or descending order of X
    myList = sorted([[Xs[i], Ys[i], Zs[i]] for i in range(len(Xs))], reverse=maxX)
    #print(myList)
# Start the Pareto frontier with the first value in the sorted list
    p_front = [myList[0]]    
# Loop through the sorted list
    for pair in myList[1:]:
        if maxY: 
            if pair[1] >= p_front[-1][1]: # Look for higher values of Y…
                p_front.append(pair) # … and add them to the Pareto frontier
        else:
            if pair[1] <= p_front[-1][1]: # Look for lower values of Y…
            	p_front.append(pair) # … and add them to the Pareto frontier
# Turn resulting pairs back into a list of Xs and Ys
    p_frontX = [pair[0] for pair in p_front]
    p_frontY = [pair[1] for pair in p_front]
    p_frontZ = [pair[2] for pair in p_front]
    return p_frontX, p_frontY, p_frontZ



num_apprx = []
sum_type = []
area = []
power = []
nmed_n = []
nmed_t = []
nmed_d = []

with open('database.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count=0
    for row in csv_reader:
        a=int(row[0])
        b=row[1]
        c=float(row[2])
        d=float(row[3])
        e=float(row[4])
        f=float(row[5])
        g=float(row[6])
        num_apprx.append(a)
        sum_type.append(b)
        area.append(c)
        power.append(d)
        nmed_n.append(e)
        nmed_t.append(f)
        nmed_d.append(g)


p_front = pareto_frontier(nmed_n, power, sum_type,maxX = False, maxY = False) 

idx = []
for m in range (len(p_front[2])):
	for k in range(len(sum_type)):
		if(p_front[2][m] == sum_type[k]):
			idx.append(k)

#idx.sort()

from prettytable import PrettyTable
t = PrettyTable(['idx', 'num aprrox', 'type', 'area', 'power', 'nmed_n'])
for i in range(len(idx)):
	t.add_row([idx[i], num_apprx[idx[i]], sum_type[idx[i]], area[idx[i]], power[idx[i]], nmed_n[idx[i]]])
print(t)

data = t.get_string()

with open('power.txt', 'w') as f:
    f.write(data)

N=len(nmed_n)
colors = np.random.rand(N)
point_area = (10 * np.random.rand(N))**2  # 0 to 15 point radii
fig0=plt.figure(0,figsize=(6,4))
ax = fig0.add_subplot(111)
plt.scatter(nmed_n, power,s=point_area, c=colors, alpha=1)
plt.plot(p_front[0], p_front[1], color="r")
ax.set_xlabel(r'Error NMED')
ax.set_ylabel(r'power (W)')
ax.grid(True)
plt.title(r'Gráfico de dispersion error nmed vs power')
plt.tight_layout()
plt.savefig("nmed_vs_power.png")


p_front = pareto_frontier(nmed_n, area, sum_type,maxX = False, maxY = False) 

idx = []
for m in range (len(p_front[2])):
	for k in range(len(sum_type)):
		if(p_front[2][m] == sum_type[k]):
			idx.append(k)

#idx.sort()

from prettytable import PrettyTable
t = PrettyTable(['idx', 'num aprrox', 'type', 'area', 'power', 'nmed_n'])
for i in range(len(idx)):
	t.add_row([idx[i], num_apprx[idx[i]], sum_type[idx[i]], area[idx[i]], power[idx[i]], nmed_n[idx[i]]])
print(t)

data = t.get_string()

with open('area.txt', 'w') as f:
    f.write(data)

N=len(nmed_n)
colors = np.random.rand(N)
point_area = (10 * np.random.rand(N))**2  # 0 to 15 point radii
fig1=plt.figure(1,figsize=(6,4))
ax = fig1.add_subplot(111)
plt.scatter(nmed_n, area,s=point_area, c=colors, alpha=1)
plt.plot(p_front[0], p_front[1], color="r")
ax.set_xlabel(r'Error NMED')
ax.set_ylabel(r'area (u2)')
ax.grid(True)
plt.title(r'Gráfico de dispersion error nmed vs area')
plt.tight_layout()
plt.savefig("nmed_vs_area.png")


metrica = []

for k in range(len(area)):
	m = area[k] * power[k]
	metrica.append(m)

p_front = pareto_frontier(nmed_n, metrica, sum_type,maxX = False, maxY = False) 

idx = []
for m in range (len(p_front[2])):
	for k in range(len(sum_type)):
		if(p_front[2][m] == sum_type[k]):
			idx.append(k)

#idx.sort()

from prettytable import PrettyTable
t = PrettyTable(['idx', 'num aprrox', 'type', 'area', 'power', 'nmed_n'])
for i in range(len(idx)):
	t.add_row([idx[i], num_apprx[idx[i]], sum_type[idx[i]], area[idx[i]], power[idx[i]], nmed_n[idx[i]]])
print(t)

data = t.get_string()

with open('metrica.txt', 'w') as f:
    f.write(data)

N=len(nmed_n)
colors = np.random.rand(N)
point_area = (10 * np.random.rand(N))**2  # 0 to 15 point radii
fig2=plt.figure(2,figsize=(6,4))
ax = fig2.add_subplot(111)
plt.scatter(nmed_n, metrica,s=point_area, c=colors, alpha=1)
plt.plot(p_front[0], p_front[1], color="r")
ax.set_xlabel(r'Error NMED')
ax.set_ylabel(r'PA')
ax.grid(True)
plt.title(r'Gráfico de dispersion error nmed vs PA')
plt.tight_layout()
plt.savefig("nmed_vs_PA.png")