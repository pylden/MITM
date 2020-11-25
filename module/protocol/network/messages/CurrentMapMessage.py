from module.protocol.network.message import Message


class CurrentMapMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 7422
        self.mapId = {"type": "Number", "value": ""}
        self.mapKey = {"type": "String", "value": ""}
