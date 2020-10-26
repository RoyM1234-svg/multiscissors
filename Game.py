class Game:
    def __init__(self):
        self.p1Went = False
        self.p2Went = False
        self.ready = False
        self.moves = [None, None]
        self.wins = [0,0]
        self.ties = 0


    def get_player_move(self, p):
        """
        :param p: [0,1]
        :return: Move
        """
        return self.moves[p]

    def play(self, player, move):
        self.moves[player] = move
        if player == 0:
            self.p1Went = True
        else:
            self.p2Went = True

    def connected(self):
        return self.ready

    def bothWent(self):
        return self.p1Went and self.p2Went

    def winner(self):

        p1 = self.moves[0]
        p2 = self.moves[1]

        if p1==p2:
            winner = -1
        elif p1 == 'paper' and p2 == 'scissors':
            winner = 1
        elif p1 == 'scissors' and p2 == 'rock':
            winner = 1
        elif p1 == 'rock' and p2 == 'paper':
            winner = 1
        else:
            winner = 0

        return winner

    def resetWent(self):
        self.p1Went = False
        self.p2Went = False