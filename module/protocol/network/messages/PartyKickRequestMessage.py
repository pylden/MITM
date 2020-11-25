from module.protocol.network.message import Message


class PartyKickRequestMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 4770
        self.playerId = {"type": "Number", "value": ""}
