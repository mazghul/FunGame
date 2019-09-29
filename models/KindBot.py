from models.Bot import Bot


class KindBot(Bot):
    def __init__(self):
        super().__init__()
        self.choice = 0
        self.name = "Kind Bot"

