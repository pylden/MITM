from module.protocol.network.message import Message


class TreasureHuntLegendaryRequestMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 5580
        self.legendaryId = {"type": "uint", "value": ""}
