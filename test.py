
import numpy as np
import matplotlib.pyplot as plt
data = np.array([0,1,2,3,4])
sum = data.sum()
mean = np.mean(data)
var = np.var(data)
print sum,mean,var
mu,sigma = 2,0.5
v = np.random.normal(mu,sigma,10000)
plt.hist(v,bins=50,normed=1)
plt.show()