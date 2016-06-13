from timer import Timer


pyramid = [[4],
         [5, 7],
        [8, 2, 6],
       [7, 1, 5, 3],
      [9, 4, 2, 6, 5],
     [7, 6, 1, 5, 7, 9],
    [3, 4, 9, 7, 1, 8, 6]]


def get_index(pyramid):
    i = 0
    j = 0
    maxes = []
    indexes = []
    for x in pyramid:
        if i == 0:
            maxes.append((max(x)))
            i += 1
            continue
        maxes.append(max(x[pyramid[i - 1].index(maxes[len(maxes) - 1])],
                         x[pyramid[i - 1].index(maxes[len(maxes) - 1]) + 1]))
        i += 1
    for x in pyramid:
        indexes.append(x.index(maxes[j]))
        j += 1
#    print maxes
#    print indexes
    return indexes


def summation(pyramid):
    pyramid_copy = [row[:] for row in pyramid]
#    print pyramid_copy
    for i in xrange(len(pyramid) - 2, -1, -1):
        for j in xrange(len(pyramid[i])):
            max_val = max(pyramid_copy[i + 1][j], pyramid_copy[i + 1][j + 1])
            pyramid_copy[i][j] += max_val
#    print pyramid_copy
    return get_index(pyramid_copy)


with Timer() as t:
    print summation(pyramid)
print "=> elasped lpush: %s s" % t.secs
