def sum_of_multiples(limit, multiples):
    items = set()
    for multiple in multiples:
       items.update(set(range(0, limit, multiple)))
    return sum(items)
