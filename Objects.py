import Constants
import numpy as np

class Election_results:

    # Initializer / Instance attributes
    def __init__(self):
        self._total_percentage_of_votes = 0
        self._invalid_votes_percentage = 0

    @property
    def total_percentage_of_votes(self):
        return self._total_percentage_of_votes

    @total_percentage_of_votes.setter
    def total_percentage_of_votes(self, value):
        # check if total sum of percentages scored by all parties does not exist 100%
        if value < 100:
            self._total_percentage_of_votes = value
            print("[Election_results class] percentage of valid votes: %s" %value)
            self.invalid_votes_percentage = 100 - self.total_percentage_of_votes
        else:
            print("[Election_results class] invalid number of valid votes: %s" %value)
            self._total_percentage_of_votes = value = 0
            raise ValueError

    @property
    def invalid_votes_percentage(self):
        return self._invalid_votes_percentage

    @invalid_votes_percentage.setter
    def invalid_votes_percentage(self, value):
        self._invalid_votes_percentage = value
        if self._invalid_votes_percentage < 0:
            raise ValueError


class Political_party:

    # Initializer / Instance attributes
    def __init__(self, name, percentage):
        self._name = name
        self._score = percentage
        self._ratio = 1.0
        self._seats = 0
        self._isBelowThreshold = True

        # scores = percentage score of a party in a constituency
        self._scores = [None] * Constants.NUMBER_OF_CONSTITUENCIES

    # increases the score of a party in the constituencies that have a lot of supporters the party
    def set_ratio(self):
        if self._name == Constants.PARTIES[Constants.PARTIES.index(self._name)]:
            self._ratio = 1.2

    # resets the ratio to default value in case a party does not have a lot supporters in a particular constituency
    def reset_ratio(self):
        self._ratio = 1.0

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        self._score = value

    @property
    def percentage(self):
        return self._percentage

    @percentage.setter
    def percentage(self, value):
        self._percentage = value

    @property
    def ratio(self):
        return self._ratio

    @ratio.setter
    def ratio(self, value):
        self._ratio= value

    @property
    def seats(self):
        return self._seats

    @seats.setter
    def seats(self, value):
        self._seats = value

    @property
    def isBelowThreshold(self):
        return self._isBelowThreshold

    @isBelowThreshold.setter
    def isBelowThreshold(self, value):
        self._isBelowThreshold = value

    @property
    def scores(self):
        return self._scores

    @scores.setter
    def scores(self, value):
        self._scores = value

    # __getitem__ and __setitem__ are used to  directly allow setting and getting specific items of the list
    def __getitem__(self, idx):
        print("getitem")
        return self._scores[idx]

    def __setitem__(self, idx, value):
        print("setitem")
        self._scores[idx] = value

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

    def calculate_scores(self, constituency):

        if self.isBelowThreshold:
            self.reset_ratio()
            self.scores[constituency.ID - 1] = self.score * self.ratio
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
            self.scores[constituency.ID - 1] *= 0.80
        # PO in LARGE_CITY_W
        if constituency.constituency_bias == Constants.Biases.LARGE_CITY_W and self.name == Constants.PARTIES[1]:
            self.scores[constituency.ID - 1] *= 1.17
        # SLD in LARGE_CITY_W
        if constituency.constituency_bias == Constants.Biases.LARGE_CITY_W and self.name == Constants.PARTIES[2]:
            self.scores[constituency.ID - 1] *= 1.05
        # KP in LARGE_CITY_W
        if constituency.constituency_bias == Constants.Biases.LARGE_CITY_W and self.name == Constants.PARTIES[3]:
            self.scores[constituency.ID - 1] *= 0.75
        # KONF in LARGE_CITY_W
        if constituency.constituency_bias == Constants.Biases.LARGE_CITY_W and self.name == Constants.PARTIES[4]:
            self.scores[constituency.ID - 1] *= 1.2

        # PiS in MEDIUM_CITY_W
        if constituency.constituency_bias == Constants.Biases.MEDIUM_CITY_W and self.name == Constants.PARTIES[0]:
            self.scores[constituency.ID - 1] *= 0.89
        # PO in MEDIUM_CITY_W
        if constituency.constituency_bias == Constants.Biases.MEDIUM_CITY_W and self.name == Constants.PARTIES[1]:
            self.scores[constituency.ID - 1] *= 1.06
        # SLD in MEDIUM_CITY_W
        if constituency.constituency_bias == Constants.Biases.MEDIUM_CITY_W and self.name == Constants.PARTIES[2]:
            self.scores[constituency.ID - 1] *= 1.05
        # KP in MEDIUM_CITY_W
        if constituency.constituency_bias == Constants.Biases.MEDIUM_CITY_W and self.name == Constants.PARTIES[3]:
            self.scores[constituency.ID - 1] *= 0.8
        # KONF in MEDIUM_CITY_W
        if constituency.constituency_bias == Constants.Biases.MEDIUM_CITY_W and self.name == Constants.PARTIES[4]:
            self.scores[constituency.ID - 1] *= 1.07

        # PiS in SMALL_CITY_W
        if constituency.constituency_bias == Constants.Biases.SMALL_CITY_W and self.name == Constants.PARTIES[0]:
            self.scores[constituency.ID - 1] *= 0.89
        # PO in SMALL_CITY_W
        if constituency.constituency_bias == Constants.Biases.SMALL_CITY_W and self.name == Constants.PARTIES[1]:
            self.scores[constituency.ID - 1] *= 1.04
        # SLD in SMALL_CITY_W
        if constituency.constituency_bias == Constants.Biases.SMALL_CITY_W and self.name == Constants.PARTIES[2]:
            self.scores[constituency.ID - 1] *= 1.05
        # KP in SMALL_CITY_W
        if constituency.constituency_bias == Constants.Biases.SMALL_CITY_W and self.name == Constants.PARTIES[3]:
            self.scores[constituency.ID - 1] *= 0.95
        # KONF in SMALL_CITY_W
        if constituency.constituency_bias == Constants.Biases.SMALL_CITY_W and self.name == Constants.PARTIES[4]:
            self.scores[constituency.ID - 1] *= 1.07

        # PiS in LARGE_CITY_E
        if constituency.constituency_bias == Constants.Biases.LARGE_CITY_E and self.name == Constants.PARTIES[0]:
            self.scores[constituency.ID - 1] *= 1.05
        # PO in LARGE_CITY_E
        if constituency.constituency_bias == Constants.Biases.LARGE_CITY_E and self.name == Constants.PARTIES[1]:
            self.scores[constituency.ID - 1] *= 0.90
        # SLD in LARGE_CITY_E
        if constituency.constituency_bias == Constants.Biases.LARGE_CITY_E and self.name == Constants.PARTIES[2]:
            self.scores[constituency.ID - 1] *= 0.9
        # KP in LARGE_CITY_E
        if constituency.constituency_bias == Constants.Biases.LARGE_CITY_E and self.name == Constants.PARTIES[3]:
            self.scores[constituency.ID - 1] *= 0.95
        # KONF in LARGE_CITY_E
        if constituency.constituency_bias == Constants.Biases.LARGE_CITY_E and self.name == Constants.PARTIES[4]:
            self.scores[constituency.ID - 1] *= 1.12

        # PiS in MEDIUM_CITY_E
        if constituency.constituency_bias == Constants.Biases.MEDIUM_CITY_E and self.name == Constants.PARTIES[0]:
            self.scores[constituency.ID - 1] *= 1.05
        # PO in MEDIUM_CITY_E
        if constituency.constituency_bias == Constants.Biases.MEDIUM_CITY_E and self.name == Constants.PARTIES[1]:
            self.scores[constituency.ID - 1] *= 0.85
        # SLD in MEDIUM_CITY_E
        if constituency.constituency_bias == Constants.Biases.MEDIUM_CITY_E and self.name == Constants.PARTIES[2]:
            self.scores[constituency.ID - 1] *= 0.9
        # KP in MEDIUM_CITY_E
        if constituency.constituency_bias == Constants.Biases.MEDIUM_CITY_E and self.name == Constants.PARTIES[3]:
            self.scores[constituency.ID - 1] *= 1.05
        # KONF in MEDIUM_CITY_E
        if constituency.constituency_bias == Constants.Biases.MEDIUM_CITY_E and self.name == Constants.PARTIES[4]:
            self.scores[constituency.ID - 1] *= 0.78

        # PiS in SMALL_CITY_E
        if constituency.constituency_bias == Constants.Biases.SMALL_CITY_E and self.name == Constants.PARTIES[0]:
            self.scores[constituency.ID - 1] *= 1.2
        # PO in SMALL_CITY_E
        if constituency.constituency_bias == Constants.Biases.SMALL_CITY_E and self.name == Constants.PARTIES[1]:
            self.scores[constituency.ID - 1] *= 0.70
        # SLD in SMALL_CITY_E
        if constituency.constituency_bias == Constants.Biases.SMALL_CITY_E and self.name == Constants.PARTIES[2]:
            self.scores[constituency.ID - 1] *= 0.8
        # KP in SMALL_CITY_E
        if constituency.constituency_bias == Constants.Biases.SMALL_CITY_E and self.name == Constants.PARTIES[3]:
            self.scores[constituency.ID - 1] *= 1.15
        # KONF in SMALL_CITY_E
        if constituency.constituency_bias == Constants.Biases.SMALL_CITY_E and self.name == Constants.PARTIES[4]:
            self.scores[constituency.ID - 1] *= 0.95

    # prints the score of a party in a constituency
    def print_score_in_constituency(self, constituency):
        print("[PoliticalParty Class] score in Constituency {0} {1} for {2}: {3: 5.2f}".format(constituency.ID,
                                    constituency.name, self.name, self.scores[constituency.ID - 1]))


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
        self.scores_for_parites = [0] * Constants.NUMBER_OF_PARTIES
        # adjusted socres to prevent from achieving more that 100% total percentage of votes in a constituency
        self.adjusted_scores_for_parites = [0] * Constants.NUMBER_OF_PARTIES
        # seats_for_parties - list of seats for each party in a constituency
        self.seats_for_parties = [0] * Constants.NUMBER_OF_PARTIES
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
        # number_of_votes_for_parties = list of total number of votes received in constituency by each party
        self.number_of_votes_for_parties = [0] * Constants.NUMBER_OF_PARTIES
        '''
        Used for calculation of number of eats received by the use of the D'Hondt method
        quotient = V / (s + 1)
        V - the total number of votes that party received
        s - the number of seats that party has been allocated so far

        Comment: 
        There have been an assumption made that none of the parties can reach more than 10 seats in a constituency.
        Therefore, only 15th first quotients are going to be calculated.
        '''

        #self.first_fifteen_quotients = [[None] * Constants.NUMBER_OF_QUOTINETS] * Constants.NUMBER_OF_PARTIES
        # we cannot define a 2D array in the above way because Python uses shallow lists:
        # first_fifteen_quotients[0][i] - points to the single list object and arr[1][i], arr[2][i] …arr[n-1][i]
        # all point to the same list object too. In the above approach there is essentially only one integer object and
        # only one list object being referenced by the all the rows of the array.

        rows, cols = Constants.NUMBER_OF_QUOTINETS, Constants.NUMBER_OF_PARTIES
        self.first_fifteen_quotients = np.array([[0 for x in range(rows)] for y in range(cols)], dtype='f')
        # the above method creates 5 separate list objects where all elements can be modified independently

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
        political_party_ID = Constants.PARTIES.index(political_party.name)
        #print("[Constituency Class] score in Constituency {0} {1} for {2}: {3: 5.2f}".format(self.ID, self.name,
        #     political_party.name, self.scores_for_parites[Constants.PARTIES.index(political_party.name)]))
        print("[Constituency Class] adjusted score in Constituency {0} {1} for {2}: {3: 5.2f}".format(self.ID, self.name,
              political_party.name, self.adjusted_scores_for_parites[political_party_ID]))
        print("[Constituency Class] Number of votes in Constituency {0} {1} for {2}: {3}".format(self.ID, self.name,
              political_party.name, self.number_of_votes_for_parties[political_party_ID]))
        #print("[Constituency Class] First 15 quotients in Constituency {0} {1} for {2}: {3}".format(self.ID, self.name,
        #     political_party.name, self.first_fifteen_quotients[political_party_ID]))

    #
    def calculate_votes_for_parties(self, political_party):
        political_party_ID = Constants.PARTIES.index(political_party.name)
        self.number_of_votes_for_parties[political_party_ID] = int(self.total_number_votes_in_constituency * \
                  self.adjusted_scores_for_parites[Constants.PARTIES.index(political_party.name)] / 100)

    # calculate_quotients function calculates first 15th quotients for each party in a constituency based on
    # the number of votes received by the party
    def calculate_quotients(self, political_party):
        political_party_ID = Constants.PARTIES.index(political_party.name)
        if ( (self.number_of_votes_for_parties[political_party_ID] >= \
            self.total_number_votes_in_constituency * Constants.ELECTION_THRESHOLD / 100) and not\
            political_party.isBelowThreshold) or ( (self.number_of_votes_for_parties[political_party_ID] >= \
            self.total_number_votes_in_constituency * Constants.ELECTION_THRESHOLD / 100) and
            political_party.name == 'MN' ):
            iterator = 0
            for quotient in range(0, Constants.NUMBER_OF_QUOTINETS):
                iterator += 1
                quotient = self.number_of_votes_for_parties[political_party_ID] / iterator
                self.first_fifteen_quotients[political_party_ID][iterator - 1] = quotient
                if iterator == Constants.NUMBER_OF_QUOTINETS:
                    iterator = 0
        else:
            for i in range (0, Constants.NUMBER_OF_QUOTINETS):
                self.first_fifteen_quotients[political_party_ID][i] = 0
