'''
Partition a list into sublists whose sums don't exceed a maximum 
    using a First Fit Decreasing algorithm. See
    http://www.ams.org/new-in-math/cover/bins1.html
    for a simple description of the method.
'''


class Bin(object):
    """ Container for items that keeps a running sum """
    def __init__(self):
        self.items = []
        self.sum = 0

    def append(self, item):
        self.items.append(item)
        self.sum += item

    def __str__(self):
        """ Printable representation """
        return 'Bin(sum=%d, items=%s)' % (self.sum, str(self.items))


def pack(values, maxValue):
    values = sorted(values, reverse=True)
    bins = []

    for item in values:
        # Try to fit item into a bin
        for bin in bins:
            if bin.sum + item <= maxValue:
                #print 'Adding', item, 'to', bin
                bin.append(item)
                break
        else:
            # item didn't fit into any bin, start a new bin
            #print 'Making new bin for', item
            bin = Bin()
            bin.append(item)
            bins.append(bin)

    return bins


if __name__ == '__main__':
    import random

    def packAndShow(aList, maxValue):
        """ Pack a list into bins and show the result """
        print('List with sum ' + str(sum(aList)) + ' requires at least ' \
        + str((sum(aList)+maxValue-1)/maxValue) + ' bins')

        bins = pack(aList, maxValue)

        print('Solution using' + str(len(bins)) + 'bins:')
        for bin in bins:
            print(str(bin))

        print


    aList = [10,9,8,7,6,5,4,3,2,1]
    packAndShow(aList, 11)

    aList = [ random.randint(1, 11) for i in range(100) ]
    packAndShow(aList, 11)

