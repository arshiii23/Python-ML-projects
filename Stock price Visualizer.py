import yfinance as yf
import matplotlib.pyplot as plt

stock = input("Enter stock (e.g. AAPL): ")

data = yf.download(stock, period="1mo")

data["Close"].plot()
plt.title(f"{stock} Stock Price")
plt.savefig("stock.png")
plt.show()