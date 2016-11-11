"""CORELLATION"""

import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

# Festlegen von Variable a und b

a, b = np.arange(1, 100),np.arange(1, 100)+10
c = [1,1,10,1,1,1,1,1,1]

# Manipolieren von Variablen
b[[1,4,14,16,19,40]] = 5
a[[0,16,30,50,98]] = 0.1

print a,b,c

mask = ~np.isnan(a) & ~np.isnan(b)
slope, intercept, r_value, p_value, std_err = stats.linregress(a[mask], b[mask])
line = slope * a + intercept

# Plot

fig = plt.figure(figsize=(18, 18))
plt.subplot(1,2,1)
ax1 = plt.scatter(a,b, color='k',label='Korrelation \n'+ str(round(r_value, 3))
                                       + r'$\pm$' + str(round(std_err, 3)))
legend = plt.legend(loc='upper left', ncol=1, fancybox=True, shadow=True,
                    fontsize ='20')
ax2 = plt.plot(a, line, 'r')
plt.grid()
plt.xlabel('Wert von a', color='blue')
plt.ylabel('Wert von b', color='green')

plt.subplot(1,2,2)
plt.plot(a, '.-b')
plt.plot(b, '.-g')
plt.grid()
plt.show()
