import csv
from decimal import Decimal

class Stock:
    _types = (str, int, float)
    __slots__ = ('name', '_shares', '_price')

    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    @classmethod
    def from_row(cls, row):
        values = [func(val) for func, val in zip(cls._types, row)]
        return cls(*values)

    @property
    def shares(self):
        return self._shares
    @shares.setter
    def shares(self, value):
        if not isinstance(value, self._types[1]):
            raise TypeError(f'Expected {self._types[1].__name__}.')
        if value < 0:
            raise ValueError('Shares must be > 0.')
        self._shares = value

    @property
    def price(self):
        return self._price
    @price.setter
    def price(self, value):
        if not isinstance(value, self._types[2]):
            raise TypeError(f'Expected {self._types[2].__name__}.')
        if value < 0:
            raise ValueError("Price must be > 0.")
        self._price = value

    @property
    def cost(self):
        return self.shares * self.price
    
    def sell(self, amount):
        if self.shares >= amount:
            self.shares -= amount
        else:
            print("Sell amount greater than share(s) available.")

class DStock(Stock):
    _types = (str, int, Decimal)

def read_portfolio(filename, class_name):
    portfolio = []
    with open(filename) as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            name = row[0]
            shares = row[1]
            price = row[2]
            stock = class_name.from_row([name, shares, price])
            portfolio.append(stock)
        
        return portfolio

def print_portfolio(portfolio):
    print('%10s %10s %10s' % ('name', 'shares', 'price'))
    print(('-'*10 + ' ')*3)
    for s in portfolio:
        print('%10s %10d %10.2f' % (s.name, s.shares, s.price))

if __name__ == '__main__':
    portfolio = read_portfolio('../../Data/portfolio.csv', Stock)
    print_portfolio(portfolio)
    
    