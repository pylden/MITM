from module.protocol.network.message import Message


class TeleportRequestMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 1080
        self.sourceType = {"type": "uint", "value": ""}
        self.destinationType = {"type": "uint", "value": ""}
        self.mapId = {"type": "Number", "value": ""}
