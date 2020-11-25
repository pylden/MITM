from module.protocol.network.message import Message


class TreasureHuntShowLegendaryUIMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 207
        self.availableLegendaryIds = {"type": "Vector.<uint>", "value": ""}
