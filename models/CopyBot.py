from models.KindBot import KindBot


class CopyBot(KindBot):
    def __init__(self):
        super().__init__()
        self.name = "Copy Cat Bot"
        self.previous_value = -1

    def get_choice(self):
        return 0 if self.previous_value == -1 else self.previous_value
