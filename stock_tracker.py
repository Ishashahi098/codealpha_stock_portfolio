# ==========================================
#        STOCK PORTFOLIO TRACKER
# ==========================================

import csv

# Hardcoded dictionary containing stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 320,
    "AMZN": 150
}

# Empty dictionary to store user's portfolio
portfolio = {}

print("===================================")
print("      STOCK PORTFOLIO TRACKER")
print("===================================")

print("\nAvailable Stocks:")

for stock, price in stock_prices.items():
    print(f"{stock} : ₹{price}")

# Taking number of stocks from user
n = int(input("\nEnter number of different stocks: "))

# Taking stock name and quantity
for i in range(n):

    print(f"\nStock {i + 1}")

    stock = input("Enter stock name: ").upper()

    if stock in stock_prices:

        quantity = int(input("Enter quantity: "))

        if quantity > 0:

            # If same stock is entered again,
            # add the quantity instead of replacing it
            if stock in portfolio:
                portfolio[stock] += quantity
            else:
                portfolio[stock] = quantity

        else:
            print("Quantity must be greater than 0.")

    else:
        print("Stock not available!")

# Calculate total investment
total_investment = 0

print("\n===================================")
print("          YOUR PORTFOLIO")
print("===================================")

for stock, quantity in portfolio.items():

    price = stock_prices[stock]

    investment = price * quantity

    total_investment += investment

    print(
        f"{stock} | Price: ₹{price} | "
        f"Quantity: {quantity} | "
        f"Investment: ₹{investment}"
    )

print("-----------------------------------")

print(f"Total Investment = ₹{total_investment}")

print("===================================")


# ==========================================
# Save portfolio in TXT file
# ==========================================

with open("portfolio.txt", "w", encoding="utf-8") as file:

    file.write("STOCK PORTFOLIO REPORT\n")
    file.write("============================\n")

    for stock, quantity in portfolio.items():

        price = stock_prices[stock]

        investment = price * quantity

        file.write(
            f"{stock} | Price: {price} | "
            f"Quantity: {quantity} | "
            f"Investment: {investment}\n"
        )

    file.write("============================\n")

    file.write(
        f"Total Investment = {total_investment}\n"
    )


# ==========================================
# Save portfolio in CSV file
# ==========================================

with open("portfolio.csv", "w", newline="") as file:

    writer = csv.writer(file)

    writer.writerow(
        ["Stock", "Price", "Quantity", "Investment"]
    )

    for stock, quantity in portfolio.items():

        price = stock_prices[stock]

        investment = price * quantity

        writer.writerow(
            [stock, price, quantity, investment]
        )

    writer.writerow([])

    writer.writerow(
        ["Total Investment", "", "", total_investment]
    )


print("\nPortfolio successfully saved!")
print("Files created:")
print("1. portfolio.txt")
print("2. portfolio.csv")