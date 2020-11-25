from module.protocol.network.message import Message


class StartupActionsAllAttributionMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 4714
        self.characterId = {"type": "Number", "value": ""}
