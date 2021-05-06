import pandas as pd
import matplotlib.cbook as plt
from sklearn.linear_model import LinearRegression
df = pd.read_csv('Profit data.csv')
fig=plt.line(df,x='Profit',y='Beans',title='plot of profit against beans')
fig.show()