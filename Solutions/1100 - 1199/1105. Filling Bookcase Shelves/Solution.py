class Solution:
    def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:
        n = len(books)
        res = [0] * (n + 1)
        for i, (j, k) in enumerate(books, 1):
            res[i] = res[i - 1] + k
            for m in range(i - 1, 0, -1):
                j += books[m - 1][0]
                if j > shelfWidth:
                    break
                k = max(k, books[m - 1][1])
                res[i] = min(res[i], res[m - 1] + k)
        return res[n]
