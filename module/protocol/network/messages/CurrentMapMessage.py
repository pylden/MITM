from module.protocol.network.message import Message


class CurrentMapMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 7422
        self.mapId = {"type": "Number", "value": ""}
        self.mapKey = {"type": "String", "value": ""}
