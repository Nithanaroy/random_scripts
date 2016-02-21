# """
# Pete is tired of spending his weekends at home and wants to leave his apartment for a nice weekend getaway. After checking Villas.com for inspiration, he found a lot of countryside accommodations in locations LL = [L1L1 .. LNLN]. Now he plans to go to LstartLstart, rent a car, travel to a few other locations from his list along the way until he reaches his final destination, location LendLend, return the car there and head back home.
#
# It doesn't matter to Pete which locations he visits, as long as the total distance that he drives in his rental car is minimal. However, his friends suggest that he not waste time and visits at least three locations. Help Pete plan a route in which both his conditions and his friends' suggestions are satisfied.
#
# Note:
#
# Pete can start and finish his route at any locations - LstartLstart, LendLend belongs to LL as long as there is a route from LstartLstart to LendLend.
# Pete wants to minimize the total driving distance of his route.
# Following his friends' suggestions, Pete wants to visit at least 3 locations.
# Pete isn't worried about the distance from his apartment to LstartLstart or the distance from LendLend back to his apartment, so you only need to minimize Pete's driving distance between LstartLstart to LendLend.
#
# Input Format
#
# The first line contains integer TT, TT test-cases follow. The first line of each test-case contains integer NN that specifies the number of locations, followed by integer MM that specifies the number of roads between locations. Locations have an id [1..N][1..N]. Each of the next MM lines contains three space separated integers AA, BB and DD, which correspond to a bi-directional road between AA and BB that has a length of DD km.
#
# Constraints
#
# 1<=T<=101<=T<=10
# 3<=N<=1053<=N<=105
# 2<=M<=4*1052<=M<=4*105
# 1<=D<=1001<=D<=100
#
# Output Format
#
# TT lines, each representing the minimal distance Pete needs to drive in km for test case ii belongs to [1..T][1..T]. Note that there always will be a valid solution.
#
# Sample Input
#
# 1
# 4 6
# 1 2 2
# 1 3 4
# 1 4 8
# 2 3 3
# 2 4 3
# 3 4 1
# Sample Output
#
# 4
# Explanation
#
# In this case, there are two possible routes that are minimized in terms of driving distance: 2 -> 3 -> 4 and 2 -> 4 -> 3, they both sum up to a total driving distance of 4. They both contain 3 different locations.
# """


def find(sets, v):
    for i, s in enumerate(sets):
        for e in s:
            if v in e[1:]:
                return i


def mst(n, edges):
    edges.sort()
    sets = []

    # every vertex is its own set
    for v in range(1, n + 1):
        sets.append([(0, v, v)])

    for e in edges:
        i1 = find(sets, e[1])
        i2 = find(sets, e[2])
        if i1 != i2:
            # both vertices do not belong to the same set

            # remove if vertex
            if len(sets[i1]) == 1 and sets[i1][0][0] == 0:
                sets[i1] = []
            if len(sets[i2]) == 1 and sets[i2][0][0] == 0:
                sets[i2] = []

            sets[i1] += sets[i2]
            sets[i1].append(e)

            if len(sets[i1]) == n - 1:  # n-1 edges are enough to connect n vertices
                return sets[i1]

            sets.pop(i2)


def minimal_distance(me):
    """
    finds 2 minimal connected edges from MST edges, me
    :param me: list of edges which form MST for the graph
    :return: distance of the chosen edges
    """
    smallest_d = 101  # given length of edge <= 100
    ismallest = -1  # index of the edge in the list, me
    for i, e in enumerate(me):
        if e[0] < smallest_d:
            smallest_d = e[0]
            ismallest = i

    d = me[ismallest][0]
    v1 = me[ismallest][1]
    v2 = me[ismallest][2]
    me.pop(ismallest)

    smallest_d = 101
    for i, e in enumerate(me):
        if (e[1] == v1 or e[2] == v1 or e[1] == v2 or e[2] == v2) and e[0] < smallest_d:
            smallest_d = e[0]

    d += smallest_d
    return d


def run():
    t = int(raw_input())  # number of test cases
    while t > 0:
        n, m = [int(i) for i in raw_input().split(" ")]
        edge_list = []
        while m > 0:
            edge = [int(i) for i in raw_input().split()]
            edge.reverse()  # so that distance comes to the first
            edge_list.append(edge)
            m -= 1
        print minimal_distance(mst(n, edge_list))
        t -= 1


def test_input():
    n = 4
    m = 6
    edge_list = [(2, 1, 2), (4, 1, 3), (8, 1, 4), (3, 2, 3), (3, 2, 4), (1, 3, 4)]  # (distance, vertex1, vertex2)
    print minimal_distance(mst(n, edge_list))


if __name__ == '__main__':
    run()

# end result - works for a few cases. Mostly timeout or runtime error
# find method is a good candidate for improving the time
