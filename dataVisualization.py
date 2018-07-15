import pandas as pd
from matplotlib import pyplot as plt
x = [1 ,2 , 3]
y = [1 , 4, 9]
z = [10 , 5 , 0]
plt.plot(x, y, z)
plt.title('test plot')
plt.xlabel("x")
plt.ylabel("y and z")
plt.legend(["this is y ", "this is z"])
#plt.show()
# Display 6 columns for viewing purposes
pd.set_option('display.max_columns', 6)

# Reduce decimal points to 2
pd.options.display.float_format = '{:,.2f}'.format

realwage = pd.read_csv('https://github.com/QuantEcon/QuantEcon.lectures.code/raw/master/pandas_panel/realwage.csv')
realwage.head()  # Show first 5 rows