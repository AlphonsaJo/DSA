
def fractional_knapsack(items, capacity):
    # Sort items by value to weight ratio in descending order
    items.sort(key=lambda item: item.ratio, reverse=True)

    total_value = 0.0  # Total value in the knapsack
    for item in items:
        if capacity - item.weight >= 0:
            # If the item can fit, add it to the knapsack
            capacity -= item.weight
            total_value += item.value
        else:
            # If the item can't fit, take the fractional part of it
            total_value += item.ratio * capacity
            break

    return total_value
