from module.protocol.network.message import Message


class AllianceFactsMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 9721
        self.leaderCharacterName = {"type": "String", "value": ""}
