import sys

BIN_SIZE = 1#1.0005 # unnecessary concern about precision errors?

# load in the items
items = [5,1,7,2,1,1,4,9]

# sort them
items.sort()

bins = []


while len(items) > 0:
    x = items.pop()
    placed = False
    # i is an index, b in the ith element
    for i, b in enumerate(bins):
        if b+x <= BIN_SIZE:
            bins[i] = b+x
            placed = True
    # if it doesn't fit in a bin, make a new one with it in it
    if not placed:
        bins.append(x)

# note: easy to figure out exact answer.
print(len(bins), bins)
