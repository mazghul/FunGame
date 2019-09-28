from models.Players import Player


class Bot(Player):
    def __init__(self, bot_type=None):
        super().__init__()
        self.bot_type = bot_type
