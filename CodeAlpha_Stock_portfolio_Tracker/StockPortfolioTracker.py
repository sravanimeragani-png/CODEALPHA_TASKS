
# Stock Portfolio Tracker

# Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 330,
    "AMZN": 150
}

total_investment = 0
portfolio_details = []

print("=" * 35)
print("     STOCK PORTFOLIO TRACKER")
print("=" * 35)

num_stocks = int(input("Enter the number of stocks: "))

for i in range(num_stocks):
    print(f"\nStock {i + 1}")

    stock_name = input("Enter stock symbol: ").upper()

    if stock_name in stock_prices:
        quantity = int(input("Enter quantity: "))

        investment = stock_prices[stock_name] * quantity
        total_investment += investment

        portfolio_details.append(
            f"{stock_name} - Quantity: {quantity} - Value: ${investment}"
        )

        print(f"Added: {stock_name}")
    else:
        print("Invalid stock symbol! Stock not found.")

print("\n" + "=" * 35)
print("       PORTFOLIO SUMMARY")
print("=" * 35)

for detail in portfolio_details:
    print(detail)

print(f"\nTotal Investment Value: ${total_investment}")

# Save summary to text file
with open("portfolio_summary.txt", "w") as file:
    file.write("STOCK PORTFOLIO SUMMARY\n")
    file.write("=" * 30 + "\n")

    for detail in portfolio_details:
        file.write(detail + "\n")

    file.write("\n")
    file.write(f"Total Investment Value: ${total_investment}")

print("\nPortfolio summary saved to 'portfolio_summary.txt'")