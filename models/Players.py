class Player:
    def __init__(self, name=None):
        self.name = name
        self.score = 0
        self.choice = None
        self.choices = []

    def get_choice(self):
        return self.choice
