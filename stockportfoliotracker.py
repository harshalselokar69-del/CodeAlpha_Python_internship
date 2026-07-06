# Stock Portfolio Tracker

# Hard-coded stock prices
stock_prices = {
    "TCS": 3500,
    "INFY": 1500,
    "RELIANCE": 2800,
    "HDFC": 1700,
    "WIPRO": 450
}

total_investment = 0

print("===== STOCK PORTFOLIO TRACKER =====")
print("Available Stocks:")

for stock, price in stock_prices.items():
    print(stock, ":", price)

num = int(input("\nHow many different stocks do you want to enter? "))

for i in range(num):
    stock_name = input("\nEnter Stock Name: ").upper()

    if stock_name in stock_prices:
        quantity = int(input("Enter Quantity: "))
        investment = stock_prices[stock_name] * quantity
        total_investment += investment
        print("Investment in", stock_name, "=", investment)
    else:
        print("Stock not found!")

print("\nTotal Investment Value =", total_investment)

# Save result to a text file
file = open("portfolio.txt", "w")
file.write("Total Investment Value = " + str(total_investment))
file.close()

print("Result saved in portfolio.txt")