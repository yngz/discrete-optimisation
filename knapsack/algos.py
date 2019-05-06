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


def dynamic_programming(capacity, items):
    """ The dimension of the table is (capacity + 1) x (#items + 1).
    Column N is the (N-1)th element in the lists (e.g. items, taken).
    """
    is_optimal = 1
    table = [[0 for c in range(len(items)+1)] for r in range(capacity+1)]

    for col in range(1, len(items)+1):  # skip 1st col, which is always 0's
        wt = items[col-1].weight
        val = items[col-1].value
        for row in range(capacity+1):
            if wt > row:  # cannot select this item
                table[row][col] = table[row][col-1]
            else:  # value of not selecting it vs selecting it
                table[row][col] = max(table[row][col-1], val + table[row-wt][col-1])
    
    # trace back for the solution
    row = capacity
    value = 0
    taken = [0] * len(items)

    for col in range(len(items), 0, -1):
        wt = items[col-1].weight
        val = items[col-1].value
        if table[row][col] > table[row][col-1]:  # the item was selected
            taken[col-1] = 1
            row -= wt
            value += val
    
    return value, is_optimal, taken
