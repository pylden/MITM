from module.protocol.network.message import Message


class ContactLookMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 6821
        self.requestId = {"type": "uint", "value": ""}
        self.playerName = {"type": "String", "value": ""}
        self.playerId = {"type": "Number", "value": ""}
        self.look = {"type": "EntityLook", "value": ""}
