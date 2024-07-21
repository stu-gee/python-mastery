import csv

class Stock:
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price
        self.headers = []
    
    def cost(self):
        return self.shares * self.price
    
    def sell(self, amount):
        if self.shares >= amount:
            self.shares -= amount
        else:
            print("Sell amount greater than share(s) available.")

def read_portfolio(filename):
    portfolio = []
    with open(filename) as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            name = row[0]
            shares = int(row[1])
            price = float(row[2])
            stock = Stock(name, shares, price)
            portfolio.append(stock)
        
        return portfolio

def print_portfolio(portfolio):
    print('%10s %10s %10s' % ('name', 'shares', 'price'))
    print(('-'*10 + ' ')*3)
    for s in portfolio:
        print('%10s %10d %10.2f' % (s.name, s.shares, s.price))

if __name__ == '__main__':
    portfolio = read_portfolio('../../Data/portfolio.csv')
    print_portfolio(portfolio)
    
    