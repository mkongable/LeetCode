class Solution(object):
    def distinctNames(self, ideas):
        """
        :type ideas: List[str]
        :rtype: int
        """
        """
        Map each character to a set of suffixes that connect with that character.
        for each pair of letters:
            get the sets associated with the two letters
            calculate the intersection of the two sets
            totalnames += (set1 - intersection) * (set2 - intersection) * 2
        return totalnames
        """

        # Map each character to a set of suffixes that connect with that character.
        char2suffixes = {}
        for idea in ideas:
            if idea[0] not in char2suffixes:
                char2suffixes[idea[0]] = set()
            char2suffixes[idea[0]].add(idea[1:])

        # iterate through all pairs of letters
        totalnames = 0
        validLetters = list(char2suffixes.keys())
        for i in range(len(validLetters)):
            for j in range(i+1, len(validLetters)):
                # get the sets associated with the two letters
                set1 = char2suffixes[validLetters[i]]
                set2 = char2suffixes[validLetters[j]]
                # calculate the intersection of the two sets
                intersection = set1.intersection(set2)
                # totalnames += (set1 - intersection) * (set2 - intersection) * 2
                totalnames += (len(set1) - len(intersection)) * (len(set2) - len(intersection)) * 2
        return totalnames