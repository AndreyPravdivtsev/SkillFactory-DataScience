
import sys
import os
import pandas as pd

import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
# python3.8 -m pip install seaborn

while True:
    try:
        mean = input("Give me a mean value of your normal distribution: ")
        mean = float(mean)
        break
    except:
        print("not a number!")

while True:
    try:
        deviation = input("Give me a standard deviation of  your normal distribution: ")
        deviation = float(deviation)
        break
    except:
        print("not a number!")

distribution_n1 = np.random.normal(0,1,1000)
distribution_n2 = np.random.normal(mean,deviation,1000)*2

dic = {"standard":distribution_n1, "user dist":distribution_n2}
df = pd.DataFrame(dic)

sns_plot = sns.displot(df, kde=True, rug=False)
# sns_plot = sns.displot(distribution_n2, kde=True, rug=False)


dirname = os.path.dirname(__file__)
codefilePath = os.path.join(dirname, 'output/' , 'plot.png')
plt.savefig(codefilePath)

print("The figure is saved successfully")