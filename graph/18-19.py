import pandas as pd
import matplotlib.pyplot as plt

dat = pd.read_csv('Microsoft_Stock.csv')

data = dat.iloc[780:1040, :]
data['Date'] = pd.to_datetime(data['Date'])

# Set the 'date' column as the index
data.set_index('Date', inplace=True)

# Plotting a line plot
plt.figure(figsize=(12, 6))
plt.plot(data.index, data['Close'], label='Value', color='red')
plt.title('Nike Sales in the year 2018 - 2019')
plt.xlabel('Date')
plt.ylabel('Value')
plt.legend()
plt.grid(True)
plt.show()
