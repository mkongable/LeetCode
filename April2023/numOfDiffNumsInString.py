def numDifferentIntegers(word):
    """
    :type word: str
    :rtype: int
    """
    # create a set
    # loop through the string
    # when we find a digit, add it to a string
    # when we find a non-digit, convert to int and add to the set
    # return the length of the set
    setOfInts = set()
    idx = 0
    while idx < len(word):
        if word[idx].isdigit():
            num = ""
            while idx < len(word) and word[idx].isdigit():
                num += word[idx]
                idx += 1
            setOfInts.add(int(num))
        idx+=1
    return len(setOfInts)
    
word = "a123bc34d8ef34"
print(numDifferentIntegers(word))