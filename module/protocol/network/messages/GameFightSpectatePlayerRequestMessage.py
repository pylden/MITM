from module.protocol.network.message import Message


class GameFightSpectatePlayerRequestMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 4807
        self.playerId = {"type": "Number", "value": ""}
