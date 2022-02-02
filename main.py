# A quick implementation of an algorithm that finds blocks in graphs.

c = 0
k = 0
s = []


class Graph:

    def __init__(self, vertices):
        self.vertices = vertices
        self.matrice = [[0 for i in range(vertices)] for j in range(vertices)]
        self.dnum = dict()
        self.low = dict()
        self.blocks = [[] * self.vertices]

    def findVertices(self, x):
        closeVertices = []
        for i in range(self.vertices):
            if self.matrice[x][i] == 1:
                closeVertices.append(i)
        return closeVertices

    # def DFSR(self, x):
    #     global s, k, c
    #     c = c + 1
    #     self.dnum[x] = c
    #     for y in range(self.vertices):
    #         if self.dnum[y] == 0:
    #             self.DFSR(y)
    #
    # def ComputeDnum(self):
    #     global s, k, c
    #     for x in range(self.vertices):
    #         self.dnum[x] = 0
    #
    #     c = 0
    #     for x in range(self.vertices):
    #         if self.dnum[x] == 0:
    #             self.DFSR(x)
    #
    # def ComputeLow(self, x):
    #     global s, k, c
    #     c = c + 1
    #     self.dnum[x] = c
    #     self.low[x] = c
    #     for y in self.findVertices(x):
    #         if self.dnum[y] == 0:
    #             self.ComputeLow(y)
    #             self.low[x] = min(self.low[x], self.low[y])
    #         else:
    #             self.low[x] = min(self.low[x], self.dnum[y])

    def newblocks(self, x, y):
        global s, k, c
        self.blocks.append([])
        self.blocks[k] = [[x]]

        while 1:
            z = s.pop()
            self.blocks[k].append([z])
            if z == y:
                break
        k = k + 1

    def findBlocks(self, x):
        global s, k, c
        c = c + 1
        self.dnum[x] = c
        self.low[x] = c
        s.append(x)
        for y in self.findVertices(x):
            if self.dnum[y] == 0:
                self.findBlocks(y)
                self.low[x] = min(self.low[x], self.low[y])
                if self.low[y] == self.dnum[x]:
                    self.newblocks(x, y)
            else:
                self.low[x] = min(self.low[x], self.dnum[y])


# Examples, don't forget to change the amount of Vertices!
ex = Graph(2)
# ex.matrice = [[0, 1, 0, 0, 1],
#               [1, 0, 0, 0, 1],
#               [0, 0, 0, 1, 1],
#               [0, 0, 1, 0, 1],
#               [1, 1, 1, 1, 0]]

# ex.matrice = [[0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
#               [1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0],
#               [0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0],
#               [1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
#               [0, 1, 1, 1, 0, 1, 0, 0, 1, 0, 0, 0],
#               [0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0],
#               [0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0],
#               [0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0],
#               [0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0],
#               [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0],
#               [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 1],
#               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0]]

# ex.matrice = [[0, 1, 0, 1],
#               [1, 0, 1, 0],
#               [0, 1, 0, 1],
#               [1, 0, 1, 0]]
ex.matrice = [[0, 1],
              [1, 0]]

for x in range(ex.vertices):
    ex.dnum[x] = 0
c = 0
k = 0
for x in range(ex.vertices):
    if ex.dnum[x] == 0:
        ex.findBlocks(x)

ex.blocks.pop()

print(ex.blocks)
print(k)
