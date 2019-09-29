from models.KindBot import KindBot


class GrudgerBot(KindBot):
    def __init__(self):
        super().__init__()
        self.name = "Copy Cat Bot"
        self.previous_value = -1

    def get_choice(self):
        return 1 if self.previous_value == 1 else 0

    def round_completed(self, value):
        if value == 1:
            self.previous_value = 1
