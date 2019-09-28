from models.Bot import Bot


class EvilBot(Bot):
    def __init__(self):
        super().__init__()
        self.choice = 1
        self.name = "Evil Bot"

    def get_choice(self):
        return self.choice
