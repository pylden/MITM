from module.protocol.network.message import Message


class ChallengeFightJoinRefusedMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 7995
        self.playerId = {"type": "Number", "value": ""}
        self.reason = {"type": "int", "value": ""}
