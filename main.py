import matplotlib.pyplot as plt

print("Hello world")

def import_data(filename):
    lines = []
    with open(filename, 'r') as f:
        l = f.read().splitlines()
        for line in l:
            line = line.strip().split(', ')
            line[1] = int(line[1])
            line[2] = float(line[2])
            lines.append(line)
    return lines


def visualize_data(data):
    # Create a dictionary to store data for each company in each country
    company_data = {}

    # Iterate over each entry in the data
    for entry in data:
        company = entry[0]
        country = entry[4]  # Assuming country information is in the fifth position [4]
        time = entry[1]  # Assuming time information is in the second position [1]
        stock_price = entry[2]

        # Create a unique key for each company in each country
        key = f"{company}_{country}"

        # If the key is not in the dictionary, create a new entry
        if key not in company_data:
            company_data[key] = {"times": [], "prices": []}

        # Append time and stock price to the respective lists
        company_data[key]["times"].append(time)
        company_data[key]["prices"].append(stock_price)

    # Create a separate plot for each company in each country
    for key, values in company_data.items():
        company, country = key.split("_")
        times = values["times"]
        prices = values["prices"]

        plt.figure(figsize=(10, 5))
        plt.plot(times, prices, marker='o', label=f"{company} - {country}")
        plt.xlabel('Time')
        plt.ylabel('Stock Price')
        plt.title(f'Stock Prices Trend for {company} in {country}')
        plt.legend()
        plt.show()

    return True
