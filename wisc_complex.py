import sys

BIN_SIZE = 10 # 1.0005 # concern about precision errors

# we use items to store... the items.
# it is a dictionary for weight to the # of copies
items = [5,1,1,8,2,5,9,4,4,1,1,9]

# this is our dynamic programming table.
# it is a dictionary, indexed by tuples
A = {}


# load in the items
'''
for line in open(sys.argv[1]):
    v = float(line)
    if v in items: items[v] += 1
    else: items[v] = 1
'''
# these things *should* be in the same order...
# so item i has counts[i] copies, each copy with weight weights[i]
counts = [items[v] for v in items]
counts = tuple(counts)
#weights = tuple(items.keys())


# now we want a list of every possible combination.
# each combination is an index into A
# first we compute the number of such combinations:
totalversions = 1
for v in items:
    totalversions *= items[v]+1

combinations = []
# this is a generalization of the base-conversion algorithm.
# trust me, it works.
for i in range(1,totalversions):
    j = i
    comb = [0 for z in range(len(counts))]
    for k in range(len(comb)):
        comb[k] = j % (counts[k]+1)
        j -= j % (counts[k]+1)
        j /= counts[k]+1
    # print comb # this shows what combination we just generated.
    combinations.append(comb[:])

# given a combination, is it a configuration (does it fit in one bin)?
def isconfig(combo):
    sum = 0.0
    for i, count in enumerate(combo):
        sum += count*weights[i]
    return sum <= BIN_SIZE # hack to avoid precision errors

# more magic. This is why learning functional programming is useful!
configurations = filter(isconfig, combinations)


# this is the "base case" (though I'm 99% sure that the configurations loop is pointless)
A[tuple([0 for i in items])] = 0
for c in configurations:
    A[tuple(c)] = 1

# this is a helper function to figure out the "priors"
def tuplesubtract(c1, c2):
    if len(c1) != len(c2): # should never happen
        print("Error in tuplesubtract: " + c1 + c2)
    res = []
    for i in range(len(c1)):
        res.append(c1[i]-c2[i])
    return tuple(res)

def tupleallnonneg(c):
    for i in c:
        if i < 0: return False
    return True

# the innermost loop in the provided psuedocode is basically a "min" function
# all this "prior" stuff captures the cleverness of the dynamic programming decomposition.
# basically: given our combination, what configurations (bins) can be *added to past combinations*
# to get our current combination? This lists those past (prior) combinations. We consider
# them in our innermost for loop
def allpriors(combo):
    for c in configurations:
        res = tuplesubtract(combo, c)
        if tupleallnonneg(res):
            yield res

# ok, fill in the table
for c in combinations:
    # this is a weird way of finding the min of all the priors
    A[tuple(c)] = min(map(lambda x: A[x], allpriors(c))) + 1

# this prints out the whole table:
#for c in combinations:
    #print A[tuple(c)], c

#this prints out the bins required.
#note that this code as-is cannot tell you how the items are arranged in bins!
print(A[tuple(combinations[-1])])
