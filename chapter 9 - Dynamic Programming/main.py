
def main():

    objects = {
        "stereo": {
            "price": 3000,
            "lb": 4
        },
        "laptop": {
            "price": 2000,
            "lb": 3
        },
        "guitar": {
            "price": 1500,
            "lb": 1
        }
    }

    items = list(objects.items())

    grid_prices = []
    grid_items = []

    for i in range(len(items)):
        row_prices = []
        row_items = []
        item_name = items[i][0]
        item_price = items[i][1]["price"]
        item_weight = items[i][1]["lb"]
        for j in range(4):
            if i == 0:
                if j + 1 == item_weight:
                    row_prices.append(item_price)
                    row_items.append([item_name])
                elif j + 1 < item_weight:
                    row_prices.append(0)
                    row_items.append(None)
            elif j + 1 == item_weight:
                if grid_prices[i - 1][j] < item_price:
                    row_prices.append(item_price)
                    row_items.append([item_name])
            elif j + 1 > item_weight:
                row_prices.append(item_price + grid_prices[i - 1][j - item_weight])
                row_items.append([item_name] + grid_items[i - 1][j - item_weight])
            else:
                row_prices.append(grid_prices[i - 1][j])
                row_items.append(grid_items[i - 1][j])

        grid_prices.append(row_prices)
        grid_items.append(row_items)

    print(grid_prices)
    print(grid_items)
    

main()
