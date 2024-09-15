def knapsack():
    products = [
        {"name": "guitar", "price": 1500, "weight": 15},
        {"name": "laptop", "price": 2000, "weight": 20},
        {"name": "stereo", "price": 3000, "weight": 30},
    ]

    sack = []
    sack_max_weight = 35

    while sack_max_weight > 0 and products:
        best = max(products, key=lambda x: x["price"]/x["weight"])
        if sack_max_weight - best["weight"] >= 0:
            sack_max_weight -= best["weight"]
            sack.append(best)
        products = [x for x in products if x != best]

    print(sack)
