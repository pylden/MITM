from module.protocol.network.message import Message


class MapComplementaryInformationsAnomalyMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 6320
        self.level = {"type": "uint", "value": ""}
        self.closingTime = {"type": "Number", "value": ""}
