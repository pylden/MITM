from module.protocol.network.message import Message


class MapComplementaryInformationsAnomalyMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 6320
        self.level = {"type": "uint", "value": ""}
        self.closingTime = {"type": "Number", "value": ""}
