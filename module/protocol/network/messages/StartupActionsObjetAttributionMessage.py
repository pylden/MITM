from module.protocol.network.message import Message


class StartupActionsObjetAttributionMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 6445
        self.actionId = {"type": "uint", "value": ""}
        self.characterId = {"type": "Number", "value": ""}
