total_value = 0.0

with open('./Data/portfolio.dat') as f:
    for line in f:
        # Split each line into components and convert the necessary parts to float
        stock_data = line.strip().split()
        shares = float(stock_data[1])
        share_cost = float(stock_data[2])
        # Calculate and accumulate the total value
        total_value += shares * share_cost

# Print the total value formatted to two decimal places
print(f"${total_value:.2f}")
