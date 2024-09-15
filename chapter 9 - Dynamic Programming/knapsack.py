import copy

def knapsack():

    goods = [
        {"name": "stereo", "price": 3000, "weight": 4},
        {"name": "guitar", "price": 1500, "weight": 1},
        {"name": "laptop", "price": 2000, "weight": 3},
        {"name": "iphone", "price": 2000, "weight": 1},
    ]
    total_weight = 4
    grid = []

    for i in range(len(goods)):
        row = []
        for j in range(total_weight):
            current_weight = j + 1  # weight starts from 1 to total_weight
            if i == 0:
                # Base case: only one item to consider
                if goods[i]["weight"] <= current_weight:
                    row.append({"estimate": goods[i]["price"], "items": [goods[i]]})
                else:
                    row.append(None)
            else:
                # Check previous row for comparison
                previous = grid[i - 1][j]
                if previous is not None:
                    # Can we add the current item?
                    if goods[i]["weight"] <= current_weight:
                        left_weight = current_weight - goods[i]["weight"]
                        if left_weight > 0 and grid[i - 1][left_weight - 1] is not None:
                            previous_copy = copy.deepcopy(grid[i - 1][left_weight - 1])
                            new_estimate = previous_copy["estimate"] + goods[i]["price"]
                            if new_estimate > previous["estimate"]:
                                previous_copy["estimate"] = new_estimate
                                previous_copy["items"].append(goods[i])
                                row.append(previous_copy)
                            else:
                                row.append(copy.deepcopy(previous))
                        else:
                            # No left weight, consider only the current item
                            if goods[i]["price"] > previous["estimate"]:
                                row.append({"estimate": goods[i]["price"], "items": [goods[i]]})
                            else:
                                row.append(copy.deepcopy(previous))
                    else:
                        row.append(copy.deepcopy(previous))
                else:
                    if goods[i]["weight"] <= current_weight:
                        row.append({"estimate": goods[i]["price"], "items": [goods[i]]})
                    else:
                        row.append(None)

        grid.append(row)

    print(grid[-1][-1])


# for i in range(len(goods)):
#     row = []
#     for j in range(total_weight):
#         if i == 0:
#             if goods[i]["weight"] <= j + 1:
#                 row.append({"estimate": goods[i]["price"], "items": [goods[i]]})
#             else:
#                 row.append(None)
#         else:
#             print(goods[i], grid[i - 1])
#             if goods[i]["price"] > grid[i - 1][j]["estimate"]:
#                 if goods[i]["weight"] == j + 1:
#                     row.append({"estimate": goods[i]["price"], "items": [goods[i]]})
#                 elif goods[i]["weight"] < j + 1:
#                     left_weight = j - goods[i]["weight"]
#                     previous = copy.deepcopy(grid[i - 1][left_weight])
#                     previous["estimate"] += goods[i]["price"]
#                     previous["items"].append(goods[i])
#                     row.append(previous)
#                 else:
#                     row.append(copy.deepcopy(grid[i - 1][j]))
#             elif goods[i]["price"] < grid[i - 1][j]["estimate"]:
#                 if goods[i]["weight"] < j + 1:
#                     left_weight = j - goods[i]["weight"]
#                     previous = copy.deepcopy(grid[i - 1][left_weight])
#                     previous["estimate"] += goods[i]["price"]
#                     previous["items"].append(goods[i])
#                     row.append(previous)
#                 else:
#                     row.append(copy.deepcopy(grid[i - 1][j]))
#             else:
#                 row.append(copy.deepcopy(grid[i - 1][j]))
#     grid.append(row)