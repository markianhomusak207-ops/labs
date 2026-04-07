class Node:
    def __init__(self, value, priority):
        self.value = value
        self.priority = priority
        self.left = None
        self.right = None
        self.height = 1

class AVLPriorityQueue:
    def __init__(self):
        self.root = None

    def insert(self, value, priority):
        self.root = self._insert(self.root, value, priority)

    def pop(self):
        if not self.root:
            raise IndexError("Черга порожня")
        self.root, node = self._remove_max(self.root)
        return node.value, node.priority

    def peek(self):
        if not self.root:
            raise IndexError("Черга порожня")
        cur = self.root
        while cur.left:
            cur = cur.left
        return cur.value, cur.priority

    def show(self):
        res = []
        self._inorder(self.root, res)
        return res

    def _h(self, n):
        return n.height if n else 0

    def _upd(self, n):
        n.height = max(self._h(n.left), self._h(n.right)) + 1

    def _bal(self, n):
        return self._h(n.left) - self._h(n.right)

    def _r(self, y):
        x = y.left
        y.left = x.right
        x.right = y
        self._upd(y)
        self._upd(x)
        return x

    def _l(self, x):
        y = x.right
        x.right = y.left
        y.left = x
        self._upd(x)
        self._upd(y)
        return y

    def _insert(self, n, v, p):
        if not n:
            return Node(v, p)

        if p >= n.priority:
            n.left = self._insert(n.left, v, p)
        else:
            n.right = self._insert(n.right, v, p)

        self._upd(n)
        b = self._bal(n)

        if b > 1 and p >= n.left.priority:
            return self._r(n)
        if b < -1 and p < n.right.priority:
            return self._l(n)
        if b > 1 and p < n.left.priority:
            n.left = self._l(n.left)
            return self._r(n)
        if b < -1 and p >= n.right.priority:
            n.right = self._r(n.right)
            return self._l(n)

        return n

    def _remove_max(self, n):
        if not n.left:
            return n.right, n

        n.left, rem = self._remove_max(n.left)
        self._upd(n)
        b = self._bal(n)

        if b > 1 and self._bal(n.left) >= 0:
            return self._r(n), rem
        if b > 1 and self._bal(n.left) < 0:
            n.left = self._l(n.left)
            return self._r(n), rem
        if b < -1 and self._bal(n.right) <= 0:
            return self._l(n), rem
        if b < -1 and self._bal(n.right) > 0:
            n.right = self._r(n.right)
            return self._l(n), rem

        return n, rem

    def _inorder(self, n, res):
        if not n:
            return
        self._inorder(n.left, res)
        res.append((n.value, n.priority))
        self._inorder(n.right, res)

if __name__ == "__main__":
    q = AVLPriorityQueue()
    q.insert("A", 3)
    q.insert("B", 7)
    q.insert("C", 5)
    q.insert("D", 9)
    q.insert("E", 1)

    print(q.show())
    print(q.peek())
    print(q.pop())
    print(q.show())