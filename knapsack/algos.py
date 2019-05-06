def greedy_trivial(capacity, items):
    """A trivial greedy algorithm for filling the knapsack.
    It takes items in-order until the knapsack is full.
    """
    value = 0
    weight = 0
    taken = [0]*len(items)
    is_optimal = 0

    for item in items:
        if weight + item.weight <= capacity:
            taken[item.index] = 1
            value += item.value
            weight += item.weight

    return value, is_optimal, taken


def greedy_density(capacity, items):
    """A simple baseline."""
    value = 0
    weight = 0
    taken = [0]*len(items)
    is_optimal = 0

    # Sort items by value-to-weight desc.
    items = sorted(items, key=lambda x: x.value / x.weight, reverse=True)

    for item in items:
        if weight + item.weight <= capacity:
            taken[item.index] = 1
            value += item.value
            weight += item.weight

    return value, is_optimal, taken
