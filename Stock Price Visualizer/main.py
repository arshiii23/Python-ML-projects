import os
import yfinance as yf
import matplotlib.pyplot as plt

# Get current file directory
base_dir = os.path.dirname(os.path.abspath(__file__))

# File path
file_path = os.path.join(base_dir, "stock.png")

stock = input("Enter stock: ")
data = yf.download(stock, period="1mo")

data["Close"].plot()
plt.title(f"{stock} Stock Price")

# Save inside project folder
plt.savefig(file_path)

plt.show()