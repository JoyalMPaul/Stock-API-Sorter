import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import yfinance as yf


file_path = "C:\\Users\\paulj\\.vscode\\stocks\\code_files\\jsons_needed\\chart.json"

df = pd.read_json(file_path, lines=True)
x_vals = df['Name'].to_list()
y_vals = df['Current Price'].to_list() 

gain_or_loss = []

for _ in range(len(x_vals)):
    stock_name = f"{x_vals[_]}"

    stock = yf.Ticker(stock_name)
    hist = stock.history(period="1d") 
    close_price = hist['Close'].iloc[0]
    
    if not hist.empty:  # Check if data is retrieved
        close_price = hist['Close'].iloc[0]
        price_change = (y_vals[_] - close_price) / close_price * 100 
        gain_or_loss.append(float(price_change)) 
    else:
        gain_or_loss.append(None)
    
x_vals.append("Total")
gain_or_loss.append(sum(gain_or_loss))

plt.figure(figsize=(12, 6))
plt.bar(x_vals, gain_or_loss, color=['red' if val < 0 else 'green' for val in gain_or_loss])  

plt.xlabel("Company", fontsize=12)
plt.ylabel("Price Change ($)", fontsize=12)
plt.title("Stock Price Changes (Current vs Last Close)", fontsize=14)
plt.xticks(rotation=45, ha='right')  
plt.grid(axis='y', linestyle='--', alpha=0.7)

plt.show()

