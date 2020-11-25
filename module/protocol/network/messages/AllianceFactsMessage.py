from module.protocol.network.message import Message


class AllianceFactsMessage(Message):
    def __init__(self):
        self.id = 9721
        self.leaderCharacterName = {"type": "String", "value": ""}
