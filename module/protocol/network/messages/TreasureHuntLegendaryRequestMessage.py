from module.protocol.network.message import Message


class TreasureHuntLegendaryRequestMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 5580
        self.legendaryId = {"type": "uint", "value": ""}
