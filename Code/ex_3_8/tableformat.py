from abc import ABC, abstractmethod

class TableFormatter(ABC):
    @abstractmethod
    def headings(self, headers):
        pass
    
    @abstractmethod
    def row(self, rowdata):
        pass

class TextTableFormatter(TableFormatter):
    def headings(self, headers):
        print(' '.join('%10s' % h for h in headers))
        print(('-'*10 + ' ')*len(headers))

    def row(self, rowdata):
        print(' '.join('%10s' % d for d in rowdata))

class CSVTableFormatter(TableFormatter):
    def headings(self, headers):
        print(','.join(f'{h}' for h in headers))

    def row(self, rowdata):
        print(','.join(f'{d}' for d in rowdata))

class HTMLTableFormatter(TableFormatter):
    def headings(self, headers):
        print('<tr>', end=' ')
        print(' '.join(f'<td>{h}</td>' for h in headers), end=' ')
        print('</tr>')

    def row(self, rowdata):
        print('<tr>', end=' ')
        print(' '.join(f'<td>{d}</td>' for d in rowdata), end=' ')
        print('</tr>')

class ColumnFormatMixin:
    formats = []
    def row(self, rowdata):
        rowdata = [(fmt % d) for fmt, d in zip(self.formats, rowdata)]
        super().row(rowdata)

class UpperHeadersMixin:
    def headings(self, headers):
        super().headings([h.upper() for h in headers])

# Print a table
def print_table(records, fields, formatter):

    # if not isinstance(formatter, TableFormatter):
    #     raise TypeError('Expected a TableFormatter')

    formatter.headings(fields)
    for r in records:
        rowdata = [getattr(r, fieldname) for fieldname in fields]
        formatter.row(rowdata)

# Create a formatter
def create_formatter(format, column_formats=None, upper_headers=False):

    formatters = {
        'HTML' : HTMLTableFormatter,
        'CSV': CSVTableFormatter,
        'TEXT': TextTableFormatter
    }

    try:
        formatter_cls = formatters[format.upper()]
    
    except KeyError:
        print(f"Unknown format: {format}.")

    if column_formats:
        class formatter_cls(ColumnFormatMixin, formatter_cls):
            formats = column_formats

    if upper_headers:
        class formatter_cls(UpperHeadersMixin, formatter_cls):
            pass

    return formatter_cls()

if __name__ == '__main__':

    import stock, reader
    from tableformat import create_formatter
    
    portfolio = reader.read_csv_as_instances('Data/portfolio.csv', stock.Stock)

    # Option #1
    #formatter = create_formatter('csv', column_formats=['"%s"','%d','%0.2f'])
    #print_table(portfolio, ['name','shares','price'], formatter)

    # Option #2
    formatter = create_formatter('text', upper_headers=True)
    print_table(portfolio, ['name','shares','price'], formatter)

