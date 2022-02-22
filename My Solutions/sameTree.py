class Solution:
    def __init__(self):
        self.same = True

    def traverse(self, t1, t2):

        if t1 and t2:

            if t1.val == t2.val:
                self.traverse(t1.left, t2.left)
                self.traverse(t1.right, t2.right)

            else:
                self.same = False

        elif not t1 and not t2:
            return

        else:
            self.same = False

    def isSameTree(self, p, q):

        if p and q:
            self.traverse(p, q)

        elif not p and not q:
            return self.same

        else:
            self.same = False

        return self.same
