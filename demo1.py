import numpy as np
import matplotlib.pyplot as plt

def h(X):
    w = np.array([20,50])
    b = -1000
    a = np.dot(X,w) + b
    return (a>=0).astype(int)
'''
X = np.array([20,10])
print(h(X)) # got 0
X = np.array([14,15])
print(h(X)) # got 1
'''
mx,my = np.meshgrid(np.linspace(0,60,200), np.linspace(0,30,200))
mX = np.array([mx.ravel(), my.ravel()]).T
mz = h(mX).reshape(200, -1)
plt.gca(aspect=1)
plt.contourf(mx,my,mz,cmap ='hot')
plt.xlabel(u' 20 bath', family='Tahoma', size =14)
plt.ylabel(u' 50 bath', family='Tahoma', size =14)
plt.show()

