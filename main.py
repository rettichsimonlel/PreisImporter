import matplotlib.pyplot as plt

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
    company_data = {}

    for entry in data:
        company = entry[0]
        country = entry[4]
        time = entry[1]
        stock_price = entry[2]

        key = f"{company}_{country}"

        if key not in company_data:
            company_data[key] = {"times": [], "prices": []}

        company_data[key]["times"].append(time)
        company_data[key]["prices"].append(stock_price)

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

def main():
    data = import_data('data.txt')
    visualize_data(data)

if __name__ == "__main__":
    main()
