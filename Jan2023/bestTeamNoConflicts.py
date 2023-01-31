def bestTeamScore(scores, ages):
    """
    :type scores: List[int]
    :type ages: List[int]
    :rtype: int
    """

    # sort the players by age

    # OPT[i] is the best score we can get if we include the ith player and only consider players with index >= i
    # OPT[i] = score[i] + the OPT[whoever is next valid]
    # return max(OPT)

    sortedPlayers = sorted(zip(ages, scores))

    # make OPT table
    OPT = [0] * len(sortedPlayers)

    OPT[-1] = sortedPlayers[-1][1]  # set the last entry to be the score of the last player

    # fill in OPT table starting from the end
    for i in range(len(sortedPlayers)-2, -1, -1):
        # always include the ith player
        # find all valid next players and take the max over all of them
        valids = []
        for j in range(i + 1, len(sortedPlayers)):
            # if its valid, take it as a possible optimal next step
            if sortedPlayers[j][1] >= sortedPlayers[i][1]:
                valids.append(OPT[j])

        # we take the best stepping stone in the end
        if len(valids) == 0:
            OPT[i] = sortedPlayers[i][1]
        else:
            OPT[i] = sortedPlayers[i][1] + max(valids)

    return max(OPT)

scores = [596,277,897,622,500,299,34,536,797,32,264,948,645,537,83,589,770]
ages = [18,52,60,79,72,28,81,33,96,15,18,5,17,96,57,72,72]
print(bestTeamScore(scores, ages))