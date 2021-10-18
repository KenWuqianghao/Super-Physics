import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

t = np.linspace(0, 10,10000)
g = 9.8
m = 2
alpha = 3
delta_t = 0.01

x = [0]
v = [0]
f_n = [m * g - alpha * v[0]]
a = [f_n[0] / m]

for i in range (1,len(t)):
    x.append(0.5*a[i - 1]*delta_t**2 + v[i - 1]*delta_t + x[i - 1])
    v.append(a[i - 1]*delta_t + v[i - 1])
    f_n.append(m * g - alpha * v[i])
    a.append(f_n[i]/m)

df = pd.DataFrame({'Time':t,'Displacement':x,'Velocity':v,'Force':f_n,'Acceleration':a})

print(df)

plt.plot(t,v)