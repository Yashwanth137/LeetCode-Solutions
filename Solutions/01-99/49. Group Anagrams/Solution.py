class Solution(object):
    def groupAnagrams(self, strs):
        d={}
        for i in strs:
            sw=''.join(sorted(i))
            if sw not in d:
                d[sw]=[i]
            else:
                d[sw].append(i)
        return list(d.values())
