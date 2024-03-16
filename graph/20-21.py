import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('oil.csv')

dataa = data.iloc[:250, :]

dataa['date'] = pd.to_datetime(dataa['date'])

dataa.set_index('date', inplace=True)

# Plotting a line plot
plt.figure(figsize=(12, 6))
plt.plot(dataa.index, dataa['dcoilwtico'], label='Value', color='red')
plt.title('Puma Sales Data in the year 2013')
plt.xlabel('Date')
plt.ylabel('Value')
plt.legend()
plt.grid(True)
plt.show()
