from module.protocol.network.message import Message


class PartyKickRequestMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 4770
        self.playerId = {"type": "Number", "value": ""}
