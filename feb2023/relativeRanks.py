def findRelativeRanks(self, score):
    """
    :type score: List[int]
    :rtype: List[str]
    """
    # create a sorted dictionary of the scores and their indices
    # iterate through the sorted dictionary, assigning the medal to the score
    # return the medals
    scoreToIndex = {}
    for i in range(len(score)):
        scoreToIndex[score[i]] = i
    sortedScoreToIndex = sorted(scoreToIndex.items(), key=lambda x: x[0], reverse=True)
    counter = 1
    for i in range(len(sortedScoreToIndex)):
        if counter == 1:
            score[sortedScoreToIndex[i][1]] = 'Gold Medal'
        elif counter == 2:
            score[sortedScoreToIndex[i][1]] = 'Silver Medal'
        elif counter == 3:
            score[sortedScoreToIndex[i][1]] = 'Bronze Medal'
        else:
            score[sortedScoreToIndex[i][1]] = str(counter)
        counter += 1
    return score