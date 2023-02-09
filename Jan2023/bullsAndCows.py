def getHint(self, secret, guess):
    """
    :type secret: str
    :type guess: str
    :rtype: str
    """
    # loop through the secret and guess
        # if secret[i] == guess[i], increment bulls
            # remove secret[i] and guess[i] from the strings
    # loop through the secret and guess
        # create a dictionary of the secret
        # create a dictionary of the guess
        # for each key in the guess dictionary
            # if the key is in the secret dictionary
                # increment cows by the minimum of the guess dictionary value and the secret dictionary value
    # return bulls and cows
    bulls = 0
    cows = 0
    for i in range(len(secret)):
        if secret[i] == guess[i]:
            bulls += 1
            secret = secret[:i] + "?" + secret[i+1:]
            guess = guess[:i] + "?" + guess[i+1:]
    secretDict = {}
    guessDict = {}
    for i in range(len(secret)):
        if secret[i] != "?" or guess[i] != "?":
            if secret[i] in secretDict:
                secretDict[secret[i]] += 1
            else:
                secretDict[secret[i]] = 1
            if guess[i] in guessDict:
                guessDict[guess[i]] += 1
            else:
                guessDict[guess[i]] = 1
    for key in guessDict:
        if key in secretDict:
            cows += min(guessDict[key], secretDict[key])
    return str(bulls) + "A" + str(cows) + "B"