import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# returns = pd.DataFrame(np.random.normal(1.0, 0.03, (100, 10)))
# prices = returns.cumprod()
# prices.plot()
# plt.show()

returns = pd.DataFrame(np.random.normal(1.0,0.03,365))

prices = returns.cumprod()

prices.plot()
plt.show()
