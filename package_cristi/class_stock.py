import pandas as pd

class Stock:
    def __init__(self):
        self.stock = pd.read_csv("stock.csv")
        self.alert_quantity = 5

    def low_stock_alert(self):
        stock_alert = [row['Product'] for index, row in self.stock.iterrows() if int(row['Quantity']) < self.alert_quantity]
        return stock_alert


if __name__ == "__main__":
    stock = Stock()
    print(stock.low_stock_alert())
