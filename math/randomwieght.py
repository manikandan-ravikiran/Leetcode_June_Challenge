class Solution(object):

    def __init__(self, w):
        """
        :type w: List[int]
        """
        self.w = list(itertools.accumulate(w))

    def pickIndex(self):
        """
        :rtype: int
        """
        return bisect.bisect_left(self.w, random.randint(1, self.w[-1]))


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()