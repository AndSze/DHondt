import sys
import Constants

class Political_party:

    # Initializer / Instance attributes
    def __init__(self, name, percentage):
        self.name = name
        self.score = percentage
        self.overall_score = 0
        self.ratio = 1.0

        # scores = percentage score of a party in a constituency
        self.scores = [None] * Constants.NUMBER_OF_CONSTITUENCIES
        # number_of_votes_in_constituency = total number of votes received in constituency by a party
        self.number_of_votes_in_constituency = [None] * Constants.NUMBER_OF_CONSTITUENCIES
        '''
        Used for calculation of number of eats received by the use of the D'Hondt method
        quotient = V / (s + 1)
        V - the total number of votes that party received
        s - the number of seats that party has been allocated so far

        Comment: 
        There have been an assumption made that none of the parties can reach more than 10 seats in a constituency.
        Therefore, only 15th first quotients are going to be calculated.
        '''
        self.first_fifteen_quotients = [None] * 15

    # increases the score of a party in the constituencies that have a lot of supporters the party
    def set_ratio(self):
        if self.name == Constants.PARTIES[Constants.PARTIES.index(self.name)]:
            self.ratio = 1.2

    # resets the ratio to default value in case a party does not have a lot supporters in a particular constituency
    def reset_ratio(self):
        self.ratio = 1.0

    ''' 
    The order of political parties in Constants.PARTIES tuple is predefined and connot be changed
    Constants.PARTIES[0] = 'PiS'
    Constants.PARTIES[1] = 'KO'
    Constants.PARTIES[2] = 'SLD'
    Constants.PARTIES[3] = 'PSL'
    Constants.PARTIES[4] = 'Konf'
    Constants.PARTIES[5] = 'BS'
    Constants.PARTIES[5] = 'MN'
    '''
    # calculates the score of a party in each constituency based on the amount of supporters and distinctive features
    def calculate_scores(self, constituency, isBelowThreshold):

        if isBelowThreshold:
            self.scores[constituency.ID - 1] = self.score
        else:
            if self.name == Constants.PARTIES[0] and constituency.isPiS:
                self.set_ratio()
                self.scores[constituency.ID - 1] = self.score * self.ratio
            elif self.name == Constants.PARTIES[1] and constituency.isKO:
                self.set_ratio()
                self.scores[constituency.ID - 1] = self.score * self.ratio
            elif self.name == Constants.PARTIES[2] and constituency.isSLD:
                self.set_ratio()
                self.scores[constituency.ID - 1] = self.score * self.ratio
            elif self.name == Constants.PARTIES[3] and constituency.isKP:
                self.set_ratio()
                self.scores[constituency.ID - 1] = self.score * self.ratio
            elif self.name == Constants.PARTIES[4] and constituency.isKonf:
                self.set_ratio()
                self.scores[constituency.ID - 1] = self.score * self.ratio
            else:
                self.reset_ratio()
                self.scores[constituency.ID - 1] = self.score * self.ratio

            # PiS in LARGE_CITY_W
            if constituency.constituency_bias == Constants.Biases.LARGE_CITY_W and self.name == Constants.PARTIES[0]:
                self.scores[constituency.ID - 1] *= 0.8
            # PO in LARGE_CITY_W
            if constituency.constituency_bias == Constants.Biases.LARGE_CITY_W and self.name == Constants.PARTIES[1]:
                self.scores[constituency.ID - 1] *= 1.2
            # SLD in LARGE_CITY_W
            if constituency.constituency_bias == Constants.Biases.LARGE_CITY_W and self.name == Constants.PARTIES[2]:
                self.scores[constituency.ID - 1] *= 1.05
            # KP in LARGE_CITY_W
            if constituency.constituency_bias == Constants.Biases.LARGE_CITY_W and self.name == Constants.PARTIES[3]:
                self.scores[constituency.ID - 1] *= 0.8
            # KONF in LARGE_CITY_W
            if constituency.constituency_bias == Constants.Biases.LARGE_CITY_W and self.name == Constants.PARTIES[4]:
                self.scores[constituency.ID - 1] *= 1.1

            # PiS in MEDIUM_CITY_W
            if constituency.constituency_bias == Constants.Biases.MEDIUM_CITY_W and self.name == Constants.PARTIES[0]:
                self.scores[constituency.ID - 1] *= 0.9
            # PO in MEDIUM_CITY_W
            if constituency.constituency_bias == Constants.Biases.MEDIUM_CITY_W and self.name == Constants.PARTIES[1]:
                self.scores[constituency.ID - 1] *= 1.1
            # SLD in MEDIUM_CITY_W
            if constituency.constituency_bias == Constants.Biases.MEDIUM_CITY_W and self.name == Constants.PARTIES[2]:
                self.scores[constituency.ID - 1] *= 1.05
            # KP in MEDIUM_CITY_W
            if constituency.constituency_bias == Constants.Biases.MEDIUM_CITY_W and self.name == Constants.PARTIES[3]:
                self.scores[constituency.ID - 1] *= 0.85
            # KONF in MEDIUM_CITY_W
            if constituency.constituency_bias == Constants.Biases.MEDIUM_CITY_W and self.name == Constants.PARTIES[4]:
                self.scores[constituency.ID - 1] *= 1.05

            # PiS in SMALL_CITY_W
            if constituency.constituency_bias == Constants.Biases.SMALL_CITY_W and self.name == Constants.PARTIES[0]:
                self.scores[constituency.ID - 1] *= 0.95
            # PO in SMALL_CITY_W
            if constituency.constituency_bias == Constants.Biases.SMALL_CITY_W and self.name == Constants.PARTIES[1]:
                self.scores[constituency.ID - 1] *= 1.05
            # SLD in SMALL_CITY_W
            if constituency.constituency_bias == Constants.Biases.SMALL_CITY_W and self.name == Constants.PARTIES[2]:
                self.scores[constituency.ID - 1] *= 1.05
            # KP in SMALL_CITY_W
            if constituency.constituency_bias == Constants.Biases.SMALL_CITY_W and self.name == Constants.PARTIES[3]:
                self.scores[constituency.ID - 1] *= 0.90
            # KONF in SMALL_CITY_W
            if constituency.constituency_bias == Constants.Biases.SMALL_CITY_W and self.name == Constants.PARTIES[4]:
                self.scores[constituency.ID - 1] *= 1.0

            # PiS in LARGE_CITY_E
            if constituency.constituency_bias == Constants.Biases.LARGE_CITY_E and self.name == Constants.PARTIES[0]:
                self.scores[constituency.ID - 1] *= 1.05
            # PO in LARGE_CITY_E
            if constituency.constituency_bias == Constants.Biases.LARGE_CITY_E and self.name == Constants.PARTIES[1]:
                self.scores[constituency.ID - 1] *= 0.95
            # SLD in LARGE_CITY_E
            if constituency.constituency_bias == Constants.Biases.LARGE_CITY_E and self.name == Constants.PARTIES[2]:
                self.scores[constituency.ID - 1] *= 0.9
            # KP in LARGE_CITY_E
            if constituency.constituency_bias == Constants.Biases.LARGE_CITY_E and self.name == Constants.PARTIES[3]:
                self.scores[constituency.ID - 1] *= 0.9
            # KONF in LARGE_CITY_E
            if constituency.constituency_bias == Constants.Biases.LARGE_CITY_E and self.name == Constants.PARTIES[4]:
                self.scores[constituency.ID - 1] *= 1.1

            # PiS in MEDIUM_CITY_E
            if constituency.constituency_bias == Constants.Biases.MEDIUM_CITY_E and self.name == Constants.PARTIES[0]:
                self.scores[constituency.ID - 1] *= 1.1
            # PO in MEDIUM_CITY_E
            if constituency.constituency_bias == Constants.Biases.MEDIUM_CITY_E and self.name == Constants.PARTIES[1]:
                self.scores[constituency.ID - 1] *= 0.9
            # SLD in MEDIUM_CITY_E
            if constituency.constituency_bias == Constants.Biases.MEDIUM_CITY_E and self.name == Constants.PARTIES[2]:
                self.scores[constituency.ID - 1] *= 0.9
            # KP in MEDIUM_CITY_E
            if constituency.constituency_bias == Constants.Biases.MEDIUM_CITY_E and self.name == Constants.PARTIES[3]:
                self.scores[constituency.ID - 1] *= 1.0
            # KONF in MEDIUM_CITY_E
            if constituency.constituency_bias == Constants.Biases.MEDIUM_CITY_E and self.name == Constants.PARTIES[4]:
                self.scores[constituency.ID - 1] *= 0.7

            # PiS in SMALL_CITY_E
            if constituency.constituency_bias == Constants.Biases.SMALL_CITY_E and self.name == Constants.PARTIES[0]:
                self.scores[constituency.ID - 1] *= 1.2
            # PO in SMALL_CITY_E
            if constituency.constituency_bias == Constants.Biases.SMALL_CITY_E and self.name == Constants.PARTIES[1]:
                self.scores[constituency.ID - 1] *= 0.8
            # SLD in SMALL_CITY_E
            if constituency.constituency_bias == Constants.Biases.SMALL_CITY_E and self.name == Constants.PARTIES[2]:
                self.scores[constituency.ID - 1] *= 0.8
            # KP in SMALL_CITY_E
            if constituency.constituency_bias == Constants.Biases.SMALL_CITY_E and self.name == Constants.PARTIES[3]:
                self.scores[constituency.ID - 1] *= 1.1
            # KONF in SMALL_CITY_E
            if constituency.constituency_bias == Constants.Biases.SMALL_CITY_E and self.name == Constants.PARTIES[4]:
                self.scores[constituency.ID - 1] *= 0.9

    # prints the score of a party in a constituency
    def print_score_in_constituency(self, constituency):
        print("[PoliticalParty Class] score in Constituency {0} {1} for {2}: {3: 5.2f}".format(constituency.ID,
                                    constituency.name, self.name, self.scores[constituency.ID - 1]))

    # calculate overall percentage score of a political party based on averaging of results in each constituency
    #def calculate_overall_score(self):
    #    self.overall_score = sum(self.scores) / Constants.NUMBER_OF_CONSTITUENCIES
    #    print("Overall score: {0}".format(self.overall_score))

    #def calculate_number_of_votes(self, constituency):
    #    self.number_of_votes = constituency.number_votes * self.overall_score


class Constituency:

    # class Initializer
    def __init__(self, name, ID, seats_number, inhabitants_number, turnout, constituency_bias):
        self.name = name
        self.ID = ID
        self.inhabitants_number = inhabitants_number
        self.seats_number = seats_number
        self.turnout = turnout
        self.constituency_bias = constituency_bias
        self.isPiS = False
        self.isKO = False
        self.isSLD = False
        self.isKP = False
        self.isKonf = False
        self.isMN = False
        self.total_number_votes_in_constituency = self.inhabitants_number * self.turnout / 100.0

        # total percentage score of a parties received in a constituency
        self.scores_for_parites = [None] * Constants.NUMBER_OF_PARTIES
        # adjusted socres to prevent from achieving more that 100% total percentage of votes in a constituency
        self.adjusted_scores_for_parites = [None] * Constants.NUMBER_OF_PARTIES
        # seats_for_parties - list of seats for each party in a constituency
        self.seats_for_parties = [None] * Constants.NUMBER_OF_PARTIES
        '''
        The order is fixed in scores_for_parites and seats_for_parties lists is fixed:
        seats_for_parties[0] = seats for PiS
        seats_for_parties[1] = seats for PO
        seats_for_parties[2] = seats for SLD
        seats_for_parties[3] = seats for PSL
        seats_for_parties[4] = seats for Konf
        seats_for_parties[5] = seats for BS
        seats_for_parties[6] = seats for MN
        '''

    # prints information about distinctive features of a constituency class object
    def print_constituency_info(self):
        print("ID: {0: <5}Name: {1: <17}Inhabitants: {2: <10}Seats: {3: <5} Turnout:{4: 5.2f}%"
              .format(self.ID, self.name, self.inhabitants_number, self.seats_number, self.turnout))
        print("likes PiS: {0}".format(self.isPiS))
        print("likes KO: {0}".format(self.isKO))
        print("likes SLD: {0}".format(self.isSLD))
        print("likes KP: {0}".format(self.isKP))
        print("likes KONF: {0}".format(self.isKonf))
        print("likes MN: {0}".format(self.isMN))
        print("")

    # assigns some distinctive features to a constituency (political parties preferences)
    def set_distinctive_features(self, isPiS, isKO, isSLD, isKP,isKonf, isMN):
        self.isPiS = isPiS
        self.isKO = isKO
        self.isSLD = isSLD
        self.isKP = isKP
        self.isKonf = isKonf
        self.isMN = isMN

    # updates elements of scores_for_parites list, which is an attribute of the constituency class
    # for making the calculations easier, it's better to keep the scores for parties as an attribute of this class
    def set_scores(self, political_party):
        score = political_party.scores[self.ID - 1]
        self.scores_for_parites[Constants.PARTIES.index(political_party.name)] = score
        #print("[Constituency Class] score in Constituency {0} {1} for {2}: {3: 5.2f}".format(self.ID, self.name,
        #      political_party.name, self.scores_for_parites[Constants.PARTIES.index(political_party.name)]))

    # adjusts the scores in each constituency to reduce the bias introduced by the amount of supporters
    # and distinctive features (the purpose of this adjustment is to have 100% total percentage score)
    def check_and_adjust_scores(self, invalid_votes_percentage):
        sum_of_scores = sum(self.scores_for_parites)
        sum_of_scores += invalid_votes_percentage
        #print("Sum of scores in constituency {0}: {1: 2.2f}".format(self.ID , sum_of_scores))
        for i in range (0, len(self.scores_for_parites)):
            self.adjusted_scores_for_parites[i] = 100 / sum_of_scores * self.scores_for_parites[i]

    # prints adjusted scores, number of votes and D'Hondt quotients for each party in a constituency
    def print_score_in_constituency(self, political_party):
        #print("[Constituency Class] score in Constituency {0} {1} for {2}: {3: 5.2f}".format(self.ID, self.name,
        #     political_party.name, self.scores_for_parites[Constants.PARTIES.index(political_party.name)]))
        print("[Constituency Class] adjusted score in Constituency {0} {1} for {2}: {3: 5.2f}".format(self.ID, self.name,
              political_party.name, self.adjusted_scores_for_parites[Constants.PARTIES.index(political_party.name)]))
        print("[Constituency Class] Number of votes in Constituency {0} {1} for {2}: {3}".format(self.ID, self.name,
              political_party.name, political_party.number_of_votes_in_constituency[self.ID -1]))
        print("[Constituency Class] First 15 quotients in Constituency {0} {1} for {2}: {3}".format(self.ID, self.name,
              political_party.name, political_party.first_fifteen_quotients))

    #
    def calculate_votes_for_parties(self, political_party):
        political_party.number_of_votes_in_constituency[self.ID -1] = int(self.total_number_votes_in_constituency * \
                  self.adjusted_scores_for_parites[Constants.PARTIES.index(political_party.name)] / 100)

    # calculate_quotients function calculates first 15th quotients for each party in a constituency based on
    # the number of votes received by the party
    def calculate_quotients(self, political_party):
        if political_party.number_of_votes_in_constituency[self.ID -1] >= \
            self.total_number_votes_in_constituency * Constants.ELECTION_THRESHOLD / 100:
            iterator = 0
            for quotient in range(0, len(political_party.first_fifteen_quotients)):
                iterator += 1
                quotient = political_party.number_of_votes_in_constituency[self.ID - 1] / iterator
                political_party.first_fifteen_quotients[iterator - 1] = quotient
        else:
            political_party.first_fifteen_quotients = [ 'N/A' ] * 15

# calculates an average value of elements in a list
def average(lst):
    return sum(lst) / len(lst)

# checks if n-th bit is set in number - used to set distinctive features for constituencies
def isNthBitSet(number, n):
    if number & (1 << (n-1)):
        return True
    else:
        return False

def main(argv):

    # input for the scores of each political party in the elections
    # The order of political parties is fixed: Pis, KO, SLD, PSL, Konf, BS, MN
    PERCENTAGES = [42.9, 23.2, 15.7, 8.6, 4.8, 2, 0.2]

    # create empty lists of constituencies and parties. In these lists the objects of Constituency and Political_party
    # classes will be stored and respectively updated
    list_of_constituencies = [None] * Constants.NUMBER_OF_CONSTITUENCIES
    list_of_political_parties = [None] * Constants.NUMBER_OF_PARTIES

    # check if total sum of percentages scored by all parties does not exist 100%
    sum_percentage = sum(PERCENTAGES)
    if sum_percentage <= 100:
        print('percentage of valid votes: %s' %sum_percentage)
    else:
        print('invalid number of valid votes: %s' %sum_percentage)
        raise ValueError
    invalid_votes_percentage = 100 - sum_percentage

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

    #for constituency in list_of_constituencies:
    #constituency.print_constituency_info()

    #sum_inhabitants = sum(Constants.INHABITANTS)
    #print("{0}".format(sum_inhabitants))

    #average_tnt = average(Constants.TURNOUT)
    #print("{0: 5.2f}".format(average_tnt))

    # for loop used for creating objects of Political_party class and setting distinctive attributes
    for i in range (0, Constants.NUMBER_OF_PARTIES):

        # create Political_party class object
        temp_party = Political_party(Constants.PARTIES[i], PERCENTAGES[i])

        # check if a party exceeded the election threshold (this rule does not apply to MN)
        if temp_party.score > Constants.ELECTION_THRESHOLD and temp_party.name != 'MN':
            isBelowElectionThreshold = False
        else:
            isBelowElectionThreshold = True

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
                temp_party.calculate_scores(temp_constituency, isBelowElectionThreshold)


            #temp_party.print_score_in_constituency(temp_constituency)

        # update i-th object of Political_party class on the list of all Political_party objects
        list_of_political_parties[i] = temp_party

        # calculate overall score
        #party_temp.calculate_overall_score()


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
        temp_constituency.check_and_adjust_scores(invalid_votes_percentage)
        # iterates through political parties to let the objects of constituency class object know which political party
        # is being processed at this time
        for temp_party in list_of_political_parties:
            temp_constituency.calculate_votes_for_parties(temp_party)
            temp_constituency.calculate_quotients(temp_party)
            temp_constituency.print_score_in_constituency(temp_party)

if __name__ == "__main__":
    main(sys.argv[0:])