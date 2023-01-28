from typing import List

def findAllConcatenatedWordsInADict(words: List[str]) -> List[str]:
    """
    :type words: List[str]
    :rtype: List[str]
    """
    d = set(words)
    
    def dfs(word):
        for i in range(1, len(word)):
            prefix = word[:i]
            suffix = word[i:]
            
            if prefix in d and suffix in d:
                return True
            if prefix in d and dfs(suffix):
                return True
            if suffix in d and dfs(prefix):
                return True
        
        return False
    
    res = []
    for word in words:
        if dfs(word):
            res.append(word)
    
    return res

words = ["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"]
print(findAllConcatenatedWordsInADict(words))