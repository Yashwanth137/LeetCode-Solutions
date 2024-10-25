class Solution:
    def removeSubfolders(self, folder: list[str]) -> list[str]:
        folder.sort()
        result = []
        prev = folder[0]
        result.append(prev)
        for i in range(1, len(folder)):
            if not folder[i].startswith(prev + "/"):
                result.append(folder[i])
                prev = folder[i]
        return result
