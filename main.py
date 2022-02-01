import numpy as np
import matplotlib.pyplot as plt
from model.model import decision
import statistics as stats

def randnum():                         
    return 10 * np.random.random() - 5

t = np.linspace(0, 20, 30)
m = [40, 10, 20, 15, 15]
weights = [0.40, 0.10, 0.10, 0.20, 0.20]
size = 70
c2b = 65
speed = 65
direction = 60
dist = 87
mean = [75, 80, 85, 89, 79]
std = [4.1, 2.7, 1.2, 3, 2]


decision, oq, options = decision(t, randnum, size, c2b, speed, direction, dist, mean, std, m, weights)

colors = ['skyblue']*(len(decision))


for i in range(len(decision)):
    if decision[i] >= 1:
        colors[i] = 'rebeccapurple'

fig = plt.figure()
ax = fig.add_axes([0, 0, 1, 1])
plt.xlabel('Time')
plt.ylabel('Quality')
ax.bar(t, oq, color = colors)



vals = []
optvals = []
for i in range(len(decision)):
    if decision[i] >= 1:
        vals.append(options[i])
        optvals.append(oq[i])

for i in range(len(vals)):
    print ((str(vals[i]) + " = " + str(optvals[i])))

print ("\n")
print (stats.fmean(vals))
print (stats.stdev(vals))

print ("\n")
print (stats.fmean(optvals))
print (stats.stdev(optvals))



