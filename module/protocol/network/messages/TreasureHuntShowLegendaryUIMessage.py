from module.protocol.network.message import Message


class TreasureHuntShowLegendaryUIMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 207
        self.availableLegendaryIds = {"type": "Vector.<uint>", "value": ""}
