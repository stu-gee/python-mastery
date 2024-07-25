class TableFormatter:
    def headings(self, headers):
        raise NotImplementedError()
    
    def row(self, rowdata):
        raise NotImplementedError()

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

# Print a table
def print_table(records, fields, formatter):
    formatter.headings(fields)
    for r in records:
        rowdata = [getattr(r, fieldname) for fieldname in fields]
        formatter.row(rowdata)

# Create a formatter
def create_formatter(format):

    formatters = {
        'HTML' : HTMLTableFormatter,
        'CSV': CSVTableFormatter,
    }

    try:
        formatter = formatters[format.upper()]
        return formatter()
    except KeyError:
        print(f"Unknown format: {format}.")