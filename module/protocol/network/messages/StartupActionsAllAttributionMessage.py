from module.protocol.network.message import Message


class StartupActionsAllAttributionMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 4714
        self.characterId = {"type": "Number", "value": ""}
