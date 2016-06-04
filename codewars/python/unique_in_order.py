def unique_in_order(iterable):
    sorted_items = []
    counter = 0
    for i in iterable:
        if len(sorted_items) == 0 or sorted_items[counter-1] != i:
            sorted_items.append(i)
            counter += counter
    return sorted_items

print(unique_in_order(['A', 'A', 'A', 'A', 'B', 'B', 'B', 'C', 'C', 'D', 'A', 'A', 'B', 'B', 'B']))
# ['A', 'A', 'A', 'A', 'B', 'B', 'B', 'C', 'C', 'D', 'A', 'A', 'B', 'B', 'B'] should equal ['A', 'B', 'C', 'D', 'A', 'B']
