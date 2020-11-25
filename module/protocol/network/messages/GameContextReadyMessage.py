from module.protocol.network.message import Message


class GameContextReadyMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 6225
        self.mapId = {"type": "Number", "value": ""}
