from module.protocol.network.message import Message


class MapInformationsRequestMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 2540
        self.mapId = {"type": "Number", "value": ""}
