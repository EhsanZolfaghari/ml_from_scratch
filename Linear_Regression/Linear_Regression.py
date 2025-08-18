import pandas as pd

data = pd.read_csv(r'D:\git\git_hub\ml_from_scratch\Linear_Regression\US-pumpkins.csv')
datahead = data.head()

#print(datahead)

data.isnull().sum()
data = data[data['Package'].str.contains('bushel', case=True, regex=True)]
selected_columns = ['Package', 'Low Price', 'High Price', 'Date']

data = data.loc[:, selected_columns]
#print(data)

price = (data['Low Price'] + data['High Price']) / 2

#print(price)

month = pd.DatetimeIndex(data['Date']).month

#print(month)


data1 = pd.DataFrame({'Month': month, 'Package': data['Package'], 'Low Price': data['Low Price'],'High Price': data['High Price'], 'Price': price})

print(data1)

data1.loc[data1['Package'].str.contains('1 1/9'), 'Price'] = price/(1 + 1/9)

data1.loc[data1['Package'].str.contains('1/2'), 'Price'] = price/(1/2)

print(data1)


import matplotlib.pyplot as plt

price = data1.Price
month = data1.Month
plt.scatter(price, month)
plt.xlabel("Pumpkin Price")
plt.ylabel("Month")
plt.show()


data1.groupby(['Month'])['Price'].mean().plot(kind='bar')
plt.ylabel("Pumpkin Price")
