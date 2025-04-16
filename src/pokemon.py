class Pokemon:
    def __init__(self, attributes):
        self.name = attributes["name"]
        self.id = attributes["id"]
        self.stats = attributes["stats"]
        self.moves = attributes["moves"]
    