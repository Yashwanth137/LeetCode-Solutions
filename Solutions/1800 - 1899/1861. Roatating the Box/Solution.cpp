class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        for row in box:
            n = len(row)
            empty = n - 1  
            for i in range(n - 1, -1, -1):
                if row[i] == '*':  
                    empty = i - 1  
                elif row[i] == '#':  
                    row[i], row[empty] = row[empty], row[i]
                    empty -= 1  

        return [list(row) for row in zip(*box[::-1])]
