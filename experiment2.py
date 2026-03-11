import matplotlib.pyplot as plt
import random
from lab3 import RBTree


class BSTNode:
    def __init__(self, v):
        self.v, self.l, self.r = v, None, None


class BST:
    def __init__(self):
        self.root = None

    def insert(self, v):
        if not self.root:
            self.root = BSTNode(v)
            return
        n = self.root
        while True:
            if v < n.v:
                if not n.l:
                    n.l = BSTNode(v)
                    return
                n = n.l
            else:
                if not n.r:
                    n.r = BSTNode(v)
                    return
                n = n.r

    def height(self):
        if not self.root:
            return 0
        q, h = [(self.root, 1)], 0
        while q:
            n, d = q.pop(0)
            h = max(h, d)
            if n.l: q.append((n.l, d+1))
            if n.r: q.append((n.r, d+1))
        return h


def gen_list(n, swaps):
    arr = list(range(n))
    for _ in range(swaps):
        i, j = random.randrange(n), random.randrange(n)
        arr[i], arr[j] = arr[j], arr[i]
    return arr


def run():
    n = 5000
    swaps = [0,1,2,5,10,20,55,100,250,750,2000]
    runs = 20

    bst_h, rbt_h, diff = [], [], []

    for s in swaps:
        b, r = 0, 0
        for _ in range(runs):
            data = gen_list(n, s)

            bst = BST()
            for v in data: bst.insert(v)
            b += bst.height()

            rbt = RBTree()
            for v in data: rbt.insert(v)
            r += rbt.get_height()

        b /= runs
        r /= runs

        bst_h.append(b)
        rbt_h.append(r)
        diff.append(b - r)

        print(f"swaps={s}, BST={b:.1f}, RBT={r:.1f}, diff={b-r:.1f}")

    plt.plot(swaps, diff, marker='o')
    plt.xscale("log")
    plt.xlabel("Number of swaps")
    plt.ylabel("Height difference")
    plt.title("Experiment 2")
    plt.grid()
    plt.show()


if __name__ == "__main__":
    run()