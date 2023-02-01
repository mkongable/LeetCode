def equalFrequency(self, word):
    """
    :type word: str
    :rtype: bool
    """
    # count the number of times each letter appears
    # if all letters appear the same number of times, return False
    # if all letters appear the same number of times except one which is greater by 1, return True
    #if all appear once return True
    # else, false
    letter_counts = {}
    for letter in word:
        if letter in letter_counts:
            letter_counts[letter] += 1
        else:
            letter_counts[letter] = 1
    letter_counts = list(letter_counts.values())
    letter_counts.sort()
    num_diff_freq = len(set(letter_counts))
    if num_diff_freq is 2:
        # can we remove 1 from something and make all the same?
        number_of_ones = letter_counts.count(1)
        if number_of_ones is 1:
            return True
        elif number_of_ones is 0:
        elif number_of_ones > 1:
            
    else:
        # num of diff freq is not 2
        if num_diff_freq is 1:
            if letter_counts[0] is 1:
                return True
            else:
                return False
        else:
            #num diff freq >= 2
            return False
    # if letter_counts[0] == letter_counts[-1]:
    #     return False
    # elif letter_counts[0] == letter_counts[-2] and letter_counts[-1] == letter_counts[-2] + 1:
    #     return True
    # elif letter_counts[0] == 1 and letter_counts[1] == letter_counts[-1]:
    #     return True
    # elif letter_counts[0] == 1 and letter_counts[-1] == 1:
    #     return True
    # else:
    #     return False
    