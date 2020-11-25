from module.protocol.network.message import Message


class AnomalyStateMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 4556
        self.subAreaId = {"type": "uint", "value": ""}
        self.open = {"type": "Boolean", "value": ""}
        self.closingTime = {"type": "Number", "value": ""}
