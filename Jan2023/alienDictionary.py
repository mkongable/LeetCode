def isAlienSorted(self, words, order):
    """
    :type words: List[str]
    :type order: str
    :rtype: bool
    """
    # Determine if the words are sorted in the alien language
    # Create a dictionary to map the order of the letters
    orderDict = {}
    for i in range(len(order)):
        orderDict[order[i]] = i
    # Compare the words
    # if the first letters are different, make sure the first letter is in the correct order
    # if the first letters are the same, compare the second letters
    # if the second letters are different, make sure the second letter is in the correct order
    # continue until the letter differs or the end of the word is reached
    for i in range(len(words)-1):
        for j in range(min(len(words[i]), len(words[i+1]))): # compare the shorter word
            if words[i][j] != words[i+1][j]: # if the letters are different
                if orderDict[words[i][j]] > orderDict[words[i+1][j]]: # if the first letter is in the wrong order
                    return False
                break
        else:
            if len(words[i]) > len(words[i+1]): # if the shorter word is the same as the longer word
                return False
    return True