def shortestCompletingWord(self, licensePlate, words):
    """
    :type licensePlate: str
    :type words: List[str]
    :rtype: str
    """
    # create a dictionary of the letters in licensePlate, ignoring case
    # loop thru words
        # create a dictionary of the letters in words[i]
        # loop thru the dictionary of licensePlate
        # if the letter is not in the dictionary of words[i]
            # break
        # if the letter is in the dictionary of words[i]
            # if the value of the letter in the dictionary of licensePlate > the letter in the dictionary of words[i]
                # break
        # if the loop finishes
            # compare the length of the shortest word to words[i]
                # set the shortest word to words[i]
    lettersInLicensePlate = {}
    for letter in licensePlate:
        if letter.isalpha():
            lettersInLicensePlate[letter.lower()] = lettersInLicensePlate.get(letter.lower(), 0) + 1
    shortestWord = ""
    for word in words:
        lettersInWords = {}
        for letter in word:
            lettersInWords[letter] = lettersInWords.get(letter, 0) + 1
        for letter in lettersInLicensePlate:
            if letter not in lettersInWords:
                break
            if lettersInLicensePlate[letter] > lettersInWords[letter]:
                break
            if letter == list(lettersInLicensePlate.keys())[-1]:
                if shortestWord == "":
                    shortestWord = word
                elif len(shortestWord) > len(word):
                    shortestWord = word
    return shortestWord

licensePlate = "1s3 PSt"
print(shortestCompletingWord(any, licensePlate, ["step", "steps", "stripe", "stepple"]))
            