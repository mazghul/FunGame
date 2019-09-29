class Tour():
    def __init__(self, t1, t2, t3, t4):
        self.t1 = t1
        self.t2 = t2
        self.t3 = t3
        self.t4 = t4
        self.game = None
        self.t1_score = 0
        self.t2_score = 0
        self.t3_score = 0
        self.t4_score = 0

    def start_tour(self, game):
        self.game = game
        self.t1_score, self.t2_score = self.tour_match(self.t1, self.t2)
        self.t1_score, self.t3_score = self.tour_match(self.t1, self.t3)
        self.t1_score, self.t4_score = self.tour_match(self.t1, self.t4)
        self.t2_score, self.t3_score = self.tour_match(self.t2, self.t3)
        self.t2_score, self.t4_score = self.tour_match(self.t2, self.t4)
        self.t3_score, self.t4_score = self.tour_match(self.t3, self.t4)
        print(
            "\n" + "-" * 20 + "Final Score Game " + str(self.t1_score) + " " + str(self.t2_score) + " " + str(
                self.t3_score) + " " + str(self.t4_score) +
            " and " + "-" * 20 + "\n")

    def tour_match(self, p1, p2):
        self.game.p_1 = p1
        self.game.p_2 = p2
        print("\n" + "-" * 20 + "Start Game " + p1.name + " and " + p2.name + "-" * 20 + "\n")
        self.game.start_game()
        self.game.print_results(self.game.p_1.score, self.game.p_2.score)
        return self.game.p_1.score, self.game.p_2.score
