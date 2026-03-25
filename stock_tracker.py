stocks = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOG": 140,
    "AMZN": 130
}

total = 0

print("Stock Portfolio Tracker")

while True:
    name = input("Enter stock name (or 'done'): ").upper()
    if name == "DONE":
        break

    if name in stocks:
        qty = int(input("Enter quantity: "))
        total += stocks[name] * qty
    else:
        print("Stock not available!")

print("Total Investment:", total)

with open("portfolio.txt", "w") as f:
    f.write(f"Total Investment: {total}")