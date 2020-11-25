from module.protocol.network.message import Message


class GameContextReadyMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 6225
        self.mapId = {"type": "Number", "value": ""}
