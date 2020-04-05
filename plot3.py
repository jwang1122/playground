import matplotlib.pyplot as plt
import numpy as np
 
x=np.arange(6)
 
fig=plt.figure()
ax=fig.add_subplot(111)
 
ax.plot(x,x,c='b',marker="^",ls='--',label='Greedy',fillstyle='none')
ax.plot(x,x+1,c='g',marker=(8,2,0),ls='--',label='Greedy Heuristic')
ax.plot(x,(x+1)**2,c='k',ls='-',label='Random')
ax.plot(x,(x-1)**2,c='r',marker="v",ls='-',label='GMC')
ax.plot(x,x**2-1,c='m',marker="o",ls='--',label='KSTW',fillstyle='none')
ax.plot(x,x-1,c='k',marker="+",ls=':',label='DGYC')
 
plt.legend(loc=2)
plt.show()