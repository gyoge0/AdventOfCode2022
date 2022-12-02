with open("day1.inp", "r") as f:
    items = f.read()

items = items.split("\n\n")
for idx, i in enumerate(items):
    items[idx] = i.split("\n")
    items[idx] = map(int, items[idx])
    items[idx] = filter(lambda x: isinstance(x, int), items[idx])
    try:
        items[idx] = sum(items[idx])
    except:
        # remove empty strings
        del items[idx]

print(sum(sorted(items, reverse=True)[:3]))
