# Print a table
def print_table(records, fields):
    print(' '.join('%10s' % fieldname for fieldname in fields))
    print(('-'*10 + ' ')*len(fields))
    for record in records:
        print(' '.join('%10s' % getattr(record, fieldname) for fieldname in fields))

if __name__ == '__main__':
    import stock

    portfolio = stock.read_portfolio('../../Data/portfolio.csv')
    print_table(portfolio, ['name','shares','price'])
