import csv

def read_csv_as_dicts(filename: str, types: list[str]) -> list[object]:
    '''
    Read CSV data into a list of dictionaries with optional type conversion
    '''
    records = []
    with open(filename) as file:
        rows = csv.reader(file)
        headers = next(rows)
        for row in rows:
            record = { name: func(val) 
                       for name, func, val in zip(headers, types, row) }
            records.append(record)
    return records

def read_csv_as_instances(filename: str, cls) -> list[object]:
    '''
    Read CSV data into a list of instances
    '''
    records = []
    with open(filename) as file:
        rows = csv.reader(file)
        headers = next(rows)
        for row in rows:
            record = cls.from_row(row)
            records.append(record)
    return records

def csv_as_dicts(lines: bytes, types: list[str], *, headers: list[str] = None):
    '''
    Take CSV data and put into a dictionary
    '''
    records = []
    rows = csv.reader(lines)

    if headers == None:
        headers = next(rows)

    for row in rows:
        record = { name: func(val)
                  for name, func, val in zip(headers, types, row) }
        records.append(record)
    return records

def csv_as_instances(lines: bytes, cls, *, headers: list[str] = None):
    '''
    Take CSV data and put into instance(s)
    '''
    records = []
    rows = csv.reader(lines)

    if headers == None:
        headers = next(rows)
    
    for row in rows:
        record = cls.from_row(row)
        records.append(record)
    return records


if __name__ == '__main__':
    import stock, gzip
    file2 = gzip.open('Data/portfolio.csv.gz', 'rt')
    file = open('Data/portfolio_noheader.csv')
    #port = csv_as_dicts(file, [str, int, float], ['name', 'shares', 'price'])
    port = csv_as_instances(file, stock.Stock)
    print(port)
    #help(csv_as_dicts)