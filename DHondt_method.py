import sys
import Constants
import numpy as np
from Objects import Election_results, Political_party, Constituency

# calculates an average value of elements in a list
def average(lst):
    return sum(lst) / len(lst)

# checks if n-th bit is set in number - used to set distinctive features for constituencies
def isNthBitSet(number, n):
    if number & (1 << (n-1)):
        return True
    else:
        return False

# input for the scores of each political party in the elections
# The order of political parties is fixed: Pis, KO, SLD, PSL, Konf, BS, MN
PERCENTAGES = [47.2, 27.4, 12.9, 6, 3.9, 1.7, 0.2]

# create empty lists of constituencies and parties. In these lists the objects of Constituency and Political_party
# classes will be stored and respectively updated
list_of_constituencies = [None] * Constants.NUMBER_OF_CONSTITUENCIES
list_of_political_parties = [None] * Constants.NUMBER_OF_PARTIES

def main(argv):

    election_results = Election_results();
    election_results.total_percentage_of_votes = sum(PERCENTAGES)

    # for loop used for creating objects of Constituency class and setting distinctive attributes
    for i in range (0, Constants.NUMBER_OF_CONSTITUENCIES):

        # create constituency class object
        temp_constituency = Constituency(Constants.CONSTITUENCY_NAMES[i],
                                         i + 1,
                                         Constants.SEATS[i],
                                         Constants.INHABITANTS[i],
                                         Constants.TURNOUT[i],
                                         Constants.CONSTITUENCY_BIASES[i])

        # set distinctive features of each constituency
        isPiSset = isNthBitSet(Constants.CONSTITUENCY_FEATURES[i], 1)
        isKOset = isNthBitSet(Constants.CONSTITUENCY_FEATURES[i], 2)
        isSLDset = isNthBitSet(Constants.CONSTITUENCY_FEATURES[i], 3)
        isKPset = isNthBitSet(Constants.CONSTITUENCY_FEATURES[i], 4)
        isKONFset = isNthBitSet(Constants.CONSTITUENCY_FEATURES[i], 5)
        isMNset = isNthBitSet(Constants.CONSTITUENCY_FEATURES[i], 6)
        temp_constituency.set_distinctive_features(isPiSset, isKOset, isSLDset, isKPset, isKONFset, isMNset)

        # update i-th object of constituency class on the list of all constituencies objects
        list_of_constituencies[i] = temp_constituency

    # for loop used for creating objects of Political_party class and setting distinctive attributes
    for i in range (0, Constants.NUMBER_OF_PARTIES):

        # create Political_party class object
        temp_party = Political_party(Constants.PARTIES[i], PERCENTAGES[i])

        # check if a party exceeded the election threshold (this rule does not apply to MN)
        if temp_party.score > Constants.ELECTION_THRESHOLD and temp_party.name != 'MN':
            temp_party.isBelowThreshold = False
        else:
            temp_party.isBelowThreshold = True

        # iterates through the list of constituency to calculate score of a party in each constituency
        for temp_constituency in list_of_constituencies:

            # uses a dedicated logic to calculate score for 'MN'
            if temp_party.name == 'MN':
                if temp_constituency.ID != 21:
                    # zeroes score for MN in the constituencies different than the 21 constituency - Opole
                    temp_party.scores[list_of_constituencies.index(temp_constituency)] = 0.0
                else:
                    # calculates score for MN in the 21th constituency - Opole
                    temp_party.scores[list_of_constituencies.index(temp_constituency)] = \
                        temp_party.score * Constants.NUMBER_OF_CONSTITUENCIES
            # uses the default function for score calculations for every political party except "MN" if the party
            # exceeded the election threshold
            else:
                temp_party.calculate_scores(temp_constituency)


            #temp_party.print_score_in_constituency(temp_constituency)

        # update i-th object of Political_party class on the list of all Political_party objects
        list_of_political_parties[i] = temp_party

    # iterates through constituencies in list_of_constituencies to set scores of each political party in every
    # constituency - the scores are saved in the attribute of the objects of Constituency class
    for temp_constituency in list_of_constituencies:
        # iterates through political parties to retrieve their scores in each constituency
        for temp_party in list_of_political_parties:
            # respective objects already stored in list_of_constituencies are being automatically updated due to
            # the fact that user-defined classes are mutable objects by default
            # mutable means: temp_constituency and list_of_constituencies[i] reference to the same locations in memory
            temp_constituency.set_scores(temp_party)

    # iterates through constituencies in list_of_constituencies to adjust scores of each political party
    for temp_constituency in list_of_constituencies:
        temp_constituency.check_and_adjust_scores(election_results.invalid_votes_percentage)
        # iterates through political parties to let the objects of constituency class object know which political party
        # is being processed at this time
        for temp_party in list_of_political_parties:
            temp_constituency.calculate_votes_for_parties(temp_party)
            temp_constituency.calculate_quotients(temp_party)
            temp_constituency.print_score_in_constituency(temp_party)

        copy_of_first_fifteen_quotients = np.copy(temp_constituency.first_fifteen_quotients)
        for i in range (0, temp_constituency.seats_number):
            result = np.where(copy_of_first_fifteen_quotients == np.amax(copy_of_first_fifteen_quotients))
            temp_constituency.seats_for_parties[result[0][0]] += 1
            copy_of_first_fifteen_quotients[result[0][0]][result[1][0]] = 0

    adjusted_scores_for_political_parties = [0] * Constants.NUMBER_OF_PARTIES
    adjusted_scores_in_constituency = [0] * Constants.NUMBER_OF_PARTIES
    for temp_constituency in list_of_constituencies:
        for i in range (0, Constants.NUMBER_OF_PARTIES):
            list_of_political_parties[i].seats += temp_constituency.seats_for_parties[i]
            adjusted_scores_for_political_parties[i] += temp_constituency.adjusted_scores_for_parites[i]
            adjusted_scores_in_constituency[i] = round(temp_constituency.adjusted_scores_for_parites[i], 2)
        print("[Main] Number of seats in constituency {0}: {1}".format(temp_constituency.name,
                                                                       temp_constituency.seats_number))
        print("[Main] Scores in Constutency {0}: {1}".format(temp_constituency.name,
                                                            adjusted_scores_in_constituency))
        print("[Main] Seats in Constutency {0}: {1}".format(temp_constituency.name,
                                                            temp_constituency.seats_for_parties))

    for i in range(0, Constants.NUMBER_OF_PARTIES):
        adjusted_scores_for_political_parties[i] = adjusted_scores_for_political_parties[i] / \
                                                   Constants.NUMBER_OF_CONSTITUENCIES
        adjusted_scores_for_political_parties[i] = round(adjusted_scores_for_political_parties[i], 2)


    print('[Main] percentage of valid votes: {0: 2.1f}'.format(election_results.total_percentage_of_votes))
    print('[Main] Adjusted scores for each political party: {0}'.format(adjusted_scores_for_political_parties))

    for temp_party in list_of_political_parties:
        print("Total number of seats for {0}: {1}".format(temp_party.name, temp_party.seats))

if __name__ == "__main__":
    main(sys.argv[0:])