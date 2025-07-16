
stock_prices = {
    "AAPL": 188,
    "TSLA": 250,
    "GOOGL": 140,
    "AMZN": 130,
    "MSFT": 370
}


portfolio = {}


num_stocks = int(input("How many stocks do you want to enter? "))


for _ in range(num_stocks):
    stock_name = input("Enter stock symbol (e.g., AAPL): ").upper()
    if stock_name in stock_prices:
        quantity = int(input(f"Enter quantity for {stock_name}: "))
        portfolio[stock_name] = quantity
    else:
        print(f"Stock {stock_name} not found in price list!")


total_investment = 0
print("\n--- Investment Summary ---")
for stock, qty in portfolio.items():
    price = stock_prices[stock]
    investment = price * qty
    total_investment += investment
    print(f"{stock}: {qty} shares × ${price} = ${investment}")

print(f"\nTotal Investment: ${total_investment}")


save_option = input("Do you want to save the result to a file? (yes/no): ").lower()
if save_option == 'yes':
    filename = "stock_portfolio.csv"
    with open(filename, 'w') as file:
        file.write("Stock,Quantity,Price,Investment\n")
        for stock, qty in portfolio.items():
            price = stock_prices[stock]
            investment = price * qty
            file.write(f"{stock},{qty},{price},{investment}\n")
        file.write(f"\nTotal Investment,,,{total_investment}")
    print(f"\nData saved to {filename}")

