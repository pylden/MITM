from module.protocol.network.message import Message


class AnomalyStateMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 4556
        self.subAreaId = {"type": "uint", "value": ""}
        self.open = {"type": "Boolean", "value": ""}
        self.closingTime = {"type": "Number", "value": ""}
