def portfolio_cost(filename):
    total_value = 0.0

    with open(filename) as f:
        for line in f:
            stock_data = line.split()
            try:
                shares = int(stock_data[1])
                share_cost = float(stock_data[2])
                total_value += shares * share_cost

            except ValueError as error:
                print(f"Couldn't parse: {line.strip()}")
                print(f"Reasons: {error}")
                print("")

        return(total_value)
        
print(portfolio_cost('Data/portfolio3.dat'))