# Stock Portfolio Tracker

A simple console-based Stock Portfolio Tracker developed using Python as part of the CodeAlpha internship task.

## Project Overview

The Stock Portfolio Tracker is a Python program that allows users to create a simple stock portfolio by entering stock names and quantities.

The program contains predefined stock prices and calculates the investment value of each selected stock using:

Investment = Stock Price × Quantity

It also calculates the total investment of the portfolio.

## Features

- Display available stocks and their prices
- Accept multiple stocks from the user
- Accept stock quantities
- Validate stock names
- Validate positive quantities
- Handle repeated stock entries
- Calculate individual stock investment
- Calculate total portfolio investment
- Save the portfolio report in TXT format
- Save the portfolio data in CSV format

## Technologies Used

- Python
- CSV module
- Dictionaries
- Loops
- Conditional Statements
- File Handling

## Predefined Stocks

The program contains the following stock prices:

| Stock | Price |
|-------|------:|
| AAPL | ₹180 |
| TSLA | ₹250 |
| GOOGL | ₹140 |
| MSFT | ₹320 |
| AMZN | ₹150 |

## How the Program Works

1. The program displays the available stocks and their prices.
2. The user enters the number of different stocks.
3. The user enters the stock name and quantity.
4. The program checks whether the stock is available.
5. The program calculates the investment for each stock.
6. The total investment is calculated.
7. The portfolio is saved into a TXT file.
8. The portfolio is also saved into a CSV file.

## Formula

```text
Investment = Stock Price × Quantity
