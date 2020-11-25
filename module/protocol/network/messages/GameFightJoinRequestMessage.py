from module.protocol.network.message import Message


class GameFightJoinRequestMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 3211
        self.fighterId = {"type": "Number", "value": ""}
        self.fightId = {"type": "uint", "value": ""}
