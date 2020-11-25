from module.protocol.network.message import Message


class StartupActionsObjetAttributionMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 6445
        self.actionId = {"type": "uint", "value": ""}
        self.characterId = {"type": "Number", "value": ""}
