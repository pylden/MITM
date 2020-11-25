from module.protocol.network.message import Message


class TeleportRequestMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 1080
        self.sourceType = {"type": "uint", "value": ""}
        self.destinationType = {"type": "uint", "value": ""}
        self.mapId = {"type": "Number", "value": ""}
