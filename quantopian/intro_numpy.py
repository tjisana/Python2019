import numpy as np
import matplotlib.pyplot as plt

# N=10
# assets = np.zeros((N,100))
# returns = np.zeros((N,100))
# R_1 = np.random.normal(1.01,0.03,100)

# returns[0] = R_1
# assets[0] = np.cumprod(R_1)

# for i in range(1,N):
#     R_i = R_1 + np.random.normal(0.001,0.02,100)
#     returns[i] = R_i
#     assets[i] = np.cumprod(R_i)

# mean_returns = [(np.mean(R) - 1)*100 for R in returns]
# return_volatilities = [np.std(R) for R in returns]

# plt.bar(np.arange(len(mean_returns)), mean_returns)
# plt.xlabel('Stock')
# plt.ylabel('Returns')
# plt.title('Returns for {0} Random Assets'.format(N))

#plt.show()

v = np.array([1, 2, np.nan, 4, 5])
ix = ~np.isnan(v) # the ~ indicates a logical not, inverting the bools
print v[ix] # We can also just write v = v[~np.isnan(v)]