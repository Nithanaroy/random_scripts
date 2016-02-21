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


class MySet:
    def __init__(self, v):
        self.v = set([])  # all vertices the set
        self.e = []  # all edges from Graph from the above set of vertices
        self.add(v)

    def add(self, v):
        self.e.append((0, v, v))
        self.v.add(v)

    # def add(self, e):
    #     self.e.append(e)
    #     # index 0 of e is the length of the edge
    #     self.v.add(e[1])
    #     self.v.add(e[2])
    #     return self  # for chaining of commands whoever is using this function

    def exists(self, v):
        return v in self.v

    def extend(self, s):
        """
        Extend the current instance by s
        :param s: instance of MySet
        :return: None
        """
        self.e += s.e
        self.v.union(s.v)


class MySetList:
    def __init__(self):
        self.s = []  # a list of MySet instances
        self.v = set([])  # a list of all vertices in the list above

    def add(self, s):
        """
        add element to list
        :param s: instance of MySet
        :return: index of this new instance in the list
        """
        self.s.append(s)
        for v in s.v:
            self.v.add(v)
        return len(self.s) - 1

    def merge(self, index1, index2):
        self.s[index2].extend(self.s[index1])
        self.s.pop(index1)
        return index2

    def edge_exists(self, e):
        """
        checks if any of the vertex of edge e is present in sets
        :param e: [v1, v2] or (v1, v2)
        :return: [i1, i2] -> list (last) indices of v1 and v2. i1 or i2 can be -1 if not found
        """
        res = [-1, -1]
        if e[0] not in self.v and e[1] not in self.v:
            return res

        for i, aset in enumerate(self.s):
            if aset.exists(e[0]):
                res[0] = i
            if aset.exists(e[1]):
                res[1] = i
        return res


def minimal_distance(n, m, edges):
    edges.sort()
    sets = MySetList()  # list of MySet instances
    for v in range(1, n + 1):
        sets.add(MySet(v))
    for e in edges:
        # sets.add(MySet(e))
        v_indices = sets.edge_exists(e[1:])
        if v_indices[0] != v_indices[1]:
            # both vertices do not belong to the same set
            sets.merge(v_indices[1], v_indices[0])
    return [e[0] for e in sets.s[0].e]


if __name__ == '__main__':
    n = 4
    m = 6
    edge_list = [(2, 1, 2), (4, 1, 3), (8, 1, 4), (3, 2, 3), (3, 2, 4), (1, 3, 4)]  # (distance, vertex1, vertex2)
    print minimal_distance(n, m, edge_list)
