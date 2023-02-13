def nextGreatestLetter(self, letters, target):
    """
    :type letters: List[str]
    :type target: str
    :rtype: str
    """
    # loop thru the list
        # if the current letter is greater than the target
            # return the current letter
    # if we get to the end of the list
        # return the first letter
    for letter in letters:
        if letter > target:
            return letter
    return letters[0]